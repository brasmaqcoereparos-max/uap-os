from app.modules.ai.assistant_facade import (
    AIAssistantFacade,
)
from app.modules.ai.project_diagnostics import (
    AIProjectDiagnostics,
)
from app.modules.ai.project_generator_service import (
    AIProjectGeneratorService,
)
from app.modules.ai.project_autocorrect import (
    AIProjectAutocorrect,
)
from app.modules.ai.project_explainer import (
    AIProjectExplainer,
)
from app.modules.ai.tool_call import (
    AIToolCall,
)
from app.modules.ai.tool_dispatcher import (
    AIToolDispatcher,
)
from app.modules.ai.tool_permission_registry import (
    ai_tool_permission_registry,
)
from app.modules.ai.tool_registry import (
    ai_tool_registry,
)


def reset_tools():
    ai_tool_registry.clear()

    ai_tool_permission_registry.clear()


def sample_project():
    return {
        "id": "project-b10",
        "name": "UAP Machine",
        "objective": (
            "Criar equipamento "
            "automatizado"
        ),
        "requirements": [
            {
                "name": (
                    "Sensor de segurança"
                ),
                "requirement_type": (
                    "safety"
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
            },
            {
                "name": (
                    "safety_boundary"
                ),
            },
        ],
    }


def test_ai_diagnostics_boundary():
    diagnostics = (
        AIProjectDiagnostics()
    )

    result = diagnostics.inspect(
        sample_project()
    )

    assert (
        result["valid"]
        is True
    )

    assert (
        result["error_count"]
        == 0
    )


def test_ai_blocks_direct_hardware():
    diagnostics = (
        AIProjectDiagnostics()
    )

    project = sample_project()

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
        finding["level"]
        == "blocked"
        for finding
        in result["findings"]
    )


def test_ai_explanation_boundary():
    explainer = (
        AIProjectExplainer()
    )

    beginner = (
        explainer.explain(
            sample_project(),
            level="beginner",
        )
    )

    professional = (
        explainer.explain(
            sample_project(),
            level="professional",
        )
    )

    assert (
        beginner["level"]
        == "beginner"
    )

    assert (
        professional["level"]
        == "professional"
    )

    professional_titles = {
        section["title"]
        for section
        in professional[
            "sections"
        ]
    }

    assert (
        "Execução"
        in professional_titles
    )


def test_ai_autocorrect_never_executes():
    autocorrect = (
        AIProjectAutocorrect()
    )

    project = {
        "name": "Project",
        "objective": (
            "Create automation"
        ),
    }

    result = (
        autocorrect.apply_safe(
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


def test_ai_project_generator_starts_unapproved():
    generator = (
        AIProjectGeneratorService()
    )

    result = generator.generate(
        name="Machine",
        objective=(
            "Automate process"
        ),
        ui_request=(
            "Create control panel"
        ),
        automation_request=(
            "Create automatic cycle"
        ),
    )

    assert (
        result["project"]
        is not None
    )

    assert (
        result["ui"]
        is not None
    )

    assert (
        result["automation"]
        is not None
    )

    assert (
        result["execution"][
            "direct_execution"
        ]
        is False
    )

    assert (
        result["execution"][
            "direct_hardware"
        ]
        is False
    )

    assert (
        result["execution"][
            "approved"
        ]
        is False
    )

    assert (
        result[
            "ready_for_execution"
        ]
        is False
    )


def test_ai_hardware_selection_is_recommendation_only():
    generator = (
        AIProjectGeneratorService()
    )

    result = generator.generate(
        name="Board Selection",
        objective=(
            "Select compatible board"
        ),
        hardware_requirements={
            "gpio": 8,
            "pwm": 2,
            "wifi": True,
        },
        boards=[
            {
                "id": "esp32",
                "name": "ESP32",
                "capabilities": {
                    "gpio": 30,
                    "pwm": 16,
                    "wifi": True,
                },
            }
        ],
    )

    assert (
        result["hardware"]
        is not None
    )

    assert (
        result["execution"][
            "direct_hardware"
        ]
        is False
    )


def test_ai_tool_project_inspection_boundary():
    reset_tools()

    dispatcher = (
        AIToolDispatcher()
    )

    result = dispatcher.dispatch(
        AIToolCall(
            tool="project.inspect",
            arguments={
                "project": (
                    sample_project()
                ),
            },
        )
    )

    assert (
        result["accepted"]
        is True
    )

    assert (
        result["status"]
        == "executed"
    )

    assert (
        result["result"][
            "metadata"
        ][
            "direct_hardware"
        ]
        is False
    )


def test_ai_tool_automation_requires_review():
    reset_tools()

    dispatcher = (
        AIToolDispatcher()
    )

    result = dispatcher.dispatch(
        AIToolCall(
            tool="automation.propose",
            arguments={
                "text": (
                    "Create motor cycle"
                ),
            },
        )
    )

    assert (
        result["accepted"]
        is True
    )

    assert (
        result["status"]
        == "review_required"
    )

    assert (
        result["result"]
        is None
    )


def test_ai_runtime_proposal_requires_review():
    reset_tools()

    dispatcher = (
        AIToolDispatcher()
    )

    result = dispatcher.dispatch(
        AIToolCall(
            tool="runtime.propose",
            arguments={
                "action": "start",
            },
        )
    )

    assert (
        result["accepted"]
        is True
    )

    assert (
        result["status"]
        == "review_required"
    )

    assert (
        result["result"]
        is None
    )


def test_ai_approved_runtime_is_still_proposal_only():
    reset_tools()

    dispatcher = (
        AIToolDispatcher()
    )

    call = AIToolCall(
        tool="runtime.propose",
        arguments={
            "action": "start",
        },
    )

    call.approve()

    result = dispatcher.dispatch(
        call
    )

    assert (
        result["status"]
        == "executed"
    )

    tool_result = (
        result["result"]
    )

    assert (
        tool_result[
            "metadata"
        ][
            "runtime_execution"
        ]
        is False
    )

    assert (
        tool_result[
            "metadata"
        ][
            "direct_hardware"
        ]
        is False
    )

    assert (
        tool_result[
            "result"
        ][
            "execute_directly"
        ]
        is False
    )


def test_direct_hardware_tool_is_rejected():
    reset_tools()

    dispatcher = (
        AIToolDispatcher()
    )

    result = dispatcher.dispatch(
        AIToolCall(
            tool=(
                "hardware.direct_write"
            ),
            arguments={
                "pin": "GPIO18",
                "value": True,
            },
        )
    )

    assert (
        result["accepted"]
        is False
    )

    assert (
        result["status"]
        == "rejected"
    )


def test_ai_assistant_facade_boundary():
    facade = (
        AIAssistantFacade()
    )

    diagnostics = (
        facade.diagnose_project(
            sample_project()
        )
    )

    explanation = (
        facade.explain_project(
            sample_project(),
            level="professional",
        )
    )

    assistance = (
        facade.project_assistance(
            sample_project(),
            level="professional",
        )
    )

    assert (
        diagnostics["valid"]
        is True
    )

    assert (
        explanation["level"]
        == "professional"
    )

    assert (
        "diagnostics"
        in assistance
    )

    assert (
        "explanation"
        in assistance
    )

    assert (
        "corrections"
        in assistance
    )

    assert (
        assistance[
            "automatic_execution"
        ]
        is False
    )

    assert (
        assistance[
            "direct_hardware"
        ]
        is False
    )


def test_block10_complete_boundary():
    generator = (
        AIProjectGeneratorService()
    )

    proposal = generator.generate(
        name="Complete UAP Project",
        objective=(
            "Create automated "
            "equipment"
        ),
        ui_request=(
            "Create operator screen"
        ),
        automation_request=(
            "Create safe sequence"
        ),
        hardware_requirements={
            "gpio": 6,
            "wifi": True,
        },
        boards=[
            {
                "id": "esp32",
                "name": "ESP32",
                "capabilities": {
                    "gpio": 30,
                    "wifi": True,
                },
            }
        ],
    )

    required_layers = {
        "project",
        "ui",
        "automation",
        "hardware",
        "execution",
        "safety",
    }

    assert (
        required_layers.issubset(
            proposal.keys()
        )
    )

    assert (
        proposal["execution"][
            "requires_validation"
        ]
        is True
    )

    assert (
        proposal["execution"][
            "requires_review"
        ]
        is True
    )

    assert (
        proposal["execution"][
            "approved"
        ]
        is False
    )

    assert (
        proposal["execution"][
            "direct_hardware"
        ]
        is False
    )

    assert (
        proposal[
            "ready_for_execution"
        ]
        is False
      )
