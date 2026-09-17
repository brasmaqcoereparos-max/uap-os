import pytest

from app.modules.runtime.runtime_context import (
    RuntimeContext,
)
from app.modules.ui.action_executor import (
    UIActionExecutor,
)
from app.modules.ui.enums import (
    ActionType,
    WidgetType,
)
from app.modules.ui.runtime_bridge import (
    UIRuntimeBridge,
)
from app.modules.ui.widget import (
    UIWidget,
)


def make_runtime_widget(
    action: str,
):
    widget = UIWidget(
        id="runtime-button",
        name="Runtime Button",
        widget_type=WidgetType.BUTTON,
    )

    widget.action_type = (
        ActionType.AUTOMATION
    )

    widget.action = {
        "runtime_action": action,
    }

    return widget


def test_runtime_bridge_requires_runtime():
    bridge = UIRuntimeBridge()

    with pytest.raises(
        RuntimeError
    ):
        bridge.execute_runtime_action(
            "start"
        )


def test_runtime_bridge_start():
    runtime = RuntimeContext(
        "project-ui-runtime"
    )

    bridge = UIRuntimeBridge()

    bridge.bind_runtime(
        runtime
    )

    result = (
        bridge.execute_runtime_action(
            "start"
        )
    )

    assert result[
        "executed"
    ] is True

    assert result[
        "action"
    ] == "start"

    assert (
        runtime.state.running
        is True
    )


def test_ui_cannot_bypass_interlock():
    runtime = RuntimeContext(
        "project-ui-interlock"
    )

    runtime.interlocks.register(
        interlock_id="door",
        name="Safety Door",
        condition=lambda: True,
    )

    bridge = UIRuntimeBridge()

    bridge.bind_runtime(
        runtime
    )

    with pytest.raises(
        RuntimeError
    ):
        bridge.execute_runtime_action(
            "start"
        )

    assert (
        runtime.state.running
        is False
    )

    assert (
        runtime.state.emergency_stop
        is True
    )


def test_ui_emergency_stop():
    runtime = RuntimeContext(
        "project-ui-estop"
    )

    bridge = UIRuntimeBridge()

    bridge.bind_runtime(
        runtime
    )

    bridge.execute_runtime_action(
        "start"
    )

    bridge.execute_runtime_action(
        "emergency_stop",
        {
            "reason": (
                "Operator UI button"
            ),
        },
    )

    assert (
        runtime.state.running
        is False
    )

    assert (
        runtime.state.emergency_stop
        is True
    )


def test_ui_cannot_restart_before_estop_reset():
    runtime = RuntimeContext(
        "project-ui-reset"
    )

    bridge = UIRuntimeBridge()

    bridge.bind_runtime(
        runtime
    )

    bridge.execute_runtime_action(
        "start"
    )

    bridge.execute_runtime_action(
        "emergency_stop"
    )

    with pytest.raises(
        RuntimeError
    ):
        bridge.execute_runtime_action(
            "start"
        )

    bridge.execute_runtime_action(
        "reset_emergency_stop"
    )

    bridge.execute_runtime_action(
        "start"
    )

    assert (
        runtime.state.running
        is True
    )


def test_ui_action_executor_uses_runtime_bridge():
    runtime = RuntimeContext(
        "project-widget-runtime"
    )

    from app.modules.ui.runtime_bridge import (
        ui_runtime_bridge,
    )

    ui_runtime_bridge.unbind_runtime()

    ui_runtime_bridge.bind_runtime(
        runtime
    )

    executor = UIActionExecutor()

    widget = make_runtime_widget(
        "start"
    )

    result = executor.execute(
        widget
    )

    assert result[
        "executed"
    ] is True

    assert (
        runtime.state.running
        is True
    )

    stop_widget = (
        make_runtime_widget(
            "stop"
        )
    )

    executor.execute(
        stop_widget
    )

    assert (
        runtime.state.running
        is False
    )

    ui_runtime_bridge.unbind_runtime()


def test_unknown_runtime_action_is_rejected():
    runtime = RuntimeContext(
        "project-invalid-action"
    )

    bridge = UIRuntimeBridge()

    bridge.bind_runtime(
        runtime
    )

    with pytest.raises(
        ValueError
    ):
        bridge.execute_runtime_action(
            "direct_gpio_write"
  )
