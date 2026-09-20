from app.modules.ai.project_autocorrect import (
    AIProjectAutocorrect,
)
from app.modules.ai.project_diagnostics import (
    AIProjectDiagnostics,
)
from app.modules.ai.project_explainer import (
    AIProjectExplainer,
)


def valid_project():
    return {
        "id": "project-1",
        "name": "Lavanderia",
        "objective": (
            "Controlar ciclo automático"
        ),
        "requirements": [
            {
                "name": (
                    "Sensor de porta"
                ),
            }
        ],
        "hardware": {
            "status": "selected",
        },
        "automation": {
            "flow": [],
        },
        "ui": {
            "screens": [],
        },
        "tests": [
            {
                "name": (
                    "simulation"
                ),
            }
        ],
    }


def test_diagnostics_accepts_complete_project():
    diagnostics = (
        AIProjectDiagnostics()
    )

    result = diagnostics.inspect(
        valid_project()
    )

    assert (
        result["valid"]
        is True
    )

    assert (
        result["error_count"]
        == 0
    )


def test_diagnostics_detects_missing_name():
    diagnostics = (
        AIProjectDiagnostics()
    )

    project = valid_project()

    project.pop(
        "name"
    )

    result = diagnostics.inspect(
        project
    )

    assert (
        result["valid"]
        is False
    )

    codes = {
        finding["code"]
        for finding
        in result["findings"]
    }

    assert (
        "missing_name"
        in codes
    )


def test_diagnostics_blocks_direct_hardware():
    diagnostics = (
        AIProjectDiagnostics()
    )

    project = valid_project()

    project[
        "direct_gpio"
    ] = {
        "pin": "GPIO18",
        "value": True,
    }

    result = diagnostics.inspect(
        project
    )

    assert (
        result["valid"]
        is False
    )

    assert any(
        finding[
            "level"
        ] == "blocked"
        for finding
        in result["findings"]
    )


def test_autocorrect_only_applies_safe_changes():
    autocorrect = (
        AIProjectAutocorrect()
    )

    project = {
        "name": "Projeto",
        "objective": (
            "Criar automação"
        ),
    }

    result = (
        autocorrect.apply_safe(
            project
        )
    )

    corrected = result[
        "project"
    ]

    assert (
        "requirements"
        in corrected
    )

    assert (
        "tests"
        in corrected
    )

    assert (
        "hardware"
        in corrected
    )

    assert (
        result[
            "automatic_execution"
        ]
        is False
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )


def test_autocorrect_does_not_fix_blocked_hardware():
    autocorrect = (
        AIProjectAutocorrect()
    )

    project = {
        "name": "Unsafe",
        "objective": "Test",
        "direct_hardware": {
            "action": "write",
        },
    }

    result = (
        autocorrect.apply_safe(
            project
        )
    )

    after = result[
        "after"
    ]

    assert (
        after["valid"]
        is False
    )

    assert any(
        finding[
            "level"
        ] == "blocked"
        for finding
        in after["findings"]
    )


def test_explainer_beginner_level():
    explainer = (
        AIProjectExplainer()
    )

    result = explainer.explain(
        valid_project(),
        level="beginner",
    )

    titles = {
        section["title"]
        for section
        in result["sections"]
    }

    assert "Objetivo" in titles
    assert "Hardware" in titles

    assert (
        "Metadados"
        not in titles
    )


def test_explainer_professional_level():
    explainer = (
        AIProjectExplainer()
    )

    project = valid_project()

    project[
        "metadata"
    ] = {
        "version": 1,
    }

    project[
        "execution"
    ] = {
        "approved": False,
    }

    result = explainer.explain(
        project,
        level="professional",
    )

    titles = {
        section["title"]
        for section
        in result["sections"]
    }

    assert "Testes" in titles
    assert "Metadados" in titles
    assert "Execução" in titles


def test_explainer_uses_diagnostics():
    explainer = (
        AIProjectExplainer()
    )

    project = valid_project()

    project.pop(
        "tests"
    )

    result = explainer.explain(
        project
    )

    assert (
        result[
            "diagnostics"
        ][
            "warning_count"
        ]
        >= 1
    )

    assert (
        result[
            "requires_review"
        ]
        is True
  )
