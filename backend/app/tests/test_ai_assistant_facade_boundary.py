from app.modules.ai.assistant_facade import (
    AIAssistantFacade,
)
from app.modules.ai.assistant_service import (
    AIAssistantService,
)


def sample_project():
    return {
        "id": "project-ai",
        "name": "UAP Machine",
        "objective": (
            "Criar máquina automatizada"
        ),
        "requirements": [
            {
                "name": (
                    "Sensor de segurança"
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
                "name": "simulation",
            }
        ],
    }


def test_assistant_diagnoses_project():
    service = AIAssistantService()

    result = (
        service.diagnose_project(
            sample_project()
        )
    )

    assert (
        result["valid"]
        is True
    )

    assert (
        result["error_count"]
        == 0
    )


def test_assistant_explains_project():
    service = AIAssistantService()

    result = (
        service.explain_project(
            sample_project(),
            level="beginner",
        )
    )

    assert (
        result["project_name"]
        == "UAP Machine"
    )

    assert (
        result["level"]
        == "beginner"
    )

    assert (
        result["sections"]
    )


def test_assistant_proposes_safe_corrections():
    service = AIAssistantService()

    project = {
        "name": "Project",
        "objective": (
            "Create automation"
        ),
    }

    result = (
        service.propose_corrections(
            project
        )
    )

    assert (
        result["requires_review"]
        is True
    )

    assert (
        result["applied"]
        is False
    )


def test_assistant_safe_correction_never_executes():
    service = AIAssistantService()

    project = {
        "name": "Project",
        "objective": (
            "Create automation"
        ),
    }

    result = (
        service.apply_safe_corrections(
            project
        )
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

    assert (
        result[
            "requires_review"
        ]
        is True
    )


def test_assistant_project_assistance_combines_services():
    service = AIAssistantService()

    result = (
        service.project_assistance(
            sample_project(),
            level="professional",
        )
    )

    assert (
        "diagnostics"
        in result
    )

    assert (
        "explanation"
        in result
    )

    assert (
        "corrections"
        in result
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


def test_facade_exposes_assistant_capabilities():
    facade = AIAssistantFacade()

    capabilities = (
        facade.capabilities()
    )

    assert (
        capabilities[
            "project"
        ][
            "enabled"
        ]
        is True
    )

    assert (
        capabilities[
            "hardware"
        ][
            "direct_execution"
        ]
        is False
    )

    assert (
        capabilities[
            "automation"
        ][
            "direct_execution"
        ]
        is False
    )


def test_facade_diagnostics():
    facade = AIAssistantFacade()

    result = (
        facade.diagnose_project(
            sample_project()
        )
    )

    assert (
        result["valid"]
        is True
    )


def test_facade_explanation_levels():
    facade = AIAssistantFacade()

    result = (
        facade.explain_project(
            sample_project(),
            level="professional",
        )
    )

    assert (
        result["level"]
        == "professional"
    )

    titles = {
        section["title"]
        for section
        in result["sections"]
    }

    assert (
        "Execução"
        in titles
    )


def test_facade_cannot_enable_direct_hardware():
    facade = AIAssistantFacade()

    project = sample_project()

    project[
        "direct_hardware"
    ] = {
        "pin": "GPIO18",
        "value": True,
    }

    result = (
        facade.diagnose_project(
            project
        )
    )

    assert (
        result["valid"]
        is False
    )

    assert any(
        finding[
            "level"
        ]
        == "blocked"
        for finding
        in result[
            "findings"
        ]
  )
