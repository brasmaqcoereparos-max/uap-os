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


def test_project_inspection_executes_without_review():
    reset_tools()

    dispatcher = AIToolDispatcher()

    result = dispatcher.dispatch(
        AIToolCall(
            tool="project.inspect",
            arguments={
                "project": {
                    "name": "Machine",
                    "objective": (
                        "Automate process"
                    ),
                    "requirements": [],
                    "tests": [],
                }
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


def test_automation_requires_review():
    reset_tools()

    dispatcher = AIToolDispatcher()

    result = dispatcher.dispatch(
        AIToolCall(
            tool="automation.propose",
            arguments={
                "text": (
                    "Criar ciclo automático"
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


def test_approved_automation_generates_proposal_only():
    reset_tools()

    dispatcher = AIToolDispatcher()

    call = AIToolCall(
        tool="automation.propose",
        arguments={
            "text": (
                "Criar ciclo automático"
            ),
        },
    )

    call.approve()

    result = dispatcher.dispatch(
        call
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
            "success"
        ]
        is True
    )

    assert (
        result["result"][
            "metadata"
        ][
            "proposal_only"
        ]
        is True
    )

    assert (
        result["result"][
            "metadata"
        ][
            "direct_hardware"
        ]
        is False
    )


def test_ui_requires_review():
    reset_tools()

    dispatcher = AIToolDispatcher()

    result = dispatcher.dispatch(
        AIToolCall(
            tool="ui.propose",
            arguments={
                "text": (
                    "Criar painel principal"
                ),
            },
        )
    )

    assert (
        result["status"]
        == "review_required"
    )


def test_runtime_proposal_requires_review():
    reset_tools()

    dispatcher = AIToolDispatcher()

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


def test_approved_runtime_still_does_not_execute():
    reset_tools()

    dispatcher = AIToolDispatcher()

    call = AIToolCall(
        tool="runtime.propose",
        arguments={
            "action": "start",
            "parameters": {},
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
        tool_result["success"]
        is True
    )

    assert (
        tool_result["result"][
            "target"
        ]
        == "runtime"
    )

    assert (
        tool_result["result"][
            "execute_directly"
        ]
        is False
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


def test_direct_hardware_tool_is_not_registered():
    reset_tools()

    dispatcher = AIToolDispatcher()

    result = dispatcher.dispatch(
        AIToolCall(
            tool="hardware.direct_write",
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


def test_hardware_inspection_is_read_only():
    reset_tools()

    dispatcher = AIToolDispatcher()

    result = dispatcher.dispatch(
        AIToolCall(
            tool="hardware.inspect",
            arguments={
                "requirements": {
                    "gpio": 4,
                    "wifi": True,
                },
                "boards": [
                    {
                        "id": "esp32",
                        "name": "ESP32",
                        "capabilities": {
                            "gpio": 30,
                            "wifi": True,
                        },
                    }
                ],
            },
        )
    )

    assert (
        result["status"]
        == "executed"
    )

    assert (
        result["result"][
            "metadata"
        ][
            "inspection_only"
        ]
        is True
    )

    assert (
        result["result"][
            "metadata"
        ][
            "direct_hardware"
        ]
        is False
    )


def test_simulation_can_execute_without_hardware():
    reset_tools()

    dispatcher = AIToolDispatcher()

    result = dispatcher.dispatch(
        AIToolCall(
            tool="simulation.propose",
            arguments={
                "name": (
                    "Machine Test"
                ),
                "inputs": [
                    {
                        "sensor": True,
                    }
                ],
                "expected_outputs": [
                    {
                        "relay": True,
                    }
                ],
            },
        )
    )

    assert (
        result["status"]
        == "executed"
    )

    assert (
        result["result"][
            "success"
        ]
        is True
    )

    assert (
        result["result"][
            "metadata"
        ][
            "simulation"
        ]
        is True
    )

    assert (
        result["result"][
            "metadata"
        ][
            "direct_hardware"
        ]
        is False
  )
