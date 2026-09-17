from app.modules.ui.action_executor import (
    ui_action_executor,
)
from app.modules.ui.binding_manager import (
    UIBindingManager,
)
from app.modules.ui.command import (
    UICommand,
)
from app.modules.ui.command_registry import (
    ui_command_registry,
)
from app.modules.ui.dialog import (
    UIDialog,
)
from app.modules.ui.dialog_manager import (
    ui_dialog_manager,
)
from app.modules.ui.enums import (
    ActionType,
    WidgetType,
)
from app.modules.ui.property_inspector import (
    UIPropertyInspector,
)
from app.modules.ui.state import (
    UIState,
)
from app.modules.ui.widget import (
    UIWidget,
)


def make_widget():
    return UIWidget(
        id="widget-1",
        name="Widget",
        widget_type=WidgetType.BUTTON,
    )


def test_property_inspector_updates_geometry():
    inspector = UIPropertyInspector()

    widget = make_widget()

    inspector.update_widget(
        widget,
        {
            "width": -10,
            "height": 200,
            "visible": "false",
        },
    )

    assert widget.width == 1
    assert widget.height == 200
    assert widget.visible is False


def test_binding_applies_state_to_widget():
    manager = UIBindingManager()

    state = UIState()

    widget = make_widget()

    manager.create(
        widget_id=widget.id,
        property_name="value",
        state_key="machine.temperature",
    )

    state.set(
        "machine.temperature",
        42,
    )

    result = (
        manager.apply_widget(
            widget,
            state,
        )
    )

    assert widget.value == 42

    assert len(result) == 1


def test_binding_write_back():
    manager = UIBindingManager()

    state = UIState()

    widget = make_widget()

    manager.create(
        widget_id=widget.id,
        property_name="value",
        state_key="machine.speed",
    )

    widget.value = 75

    manager.write_back(
        widget,
        state,
    )

    assert (
        state.get(
            "machine.speed"
        )
        == 75
    )


def test_command_action_executes_command():
    widget = make_widget()

    command = UICommand(
        id="test.command",
        name="Test Command",
        handler=lambda data: {
            "value": data.get(
                "value"
            )
        },
    )

    ui_command_registry.register(
        command
    )

    widget.action_type = (
        ActionType.COMMAND
    )

    widget.action = {
        "command_id": (
            "test.command"
        ),
    }

    result = (
        ui_action_executor.execute(
            widget,
            {
                "value": 123,
            },
        )
    )

    assert result[
        "executed"
    ] is True

    assert result[
        "result"
    ]["value"] == 123

    ui_command_registry.remove(
        "test.command"
    )


def test_open_and_close_dialog_action():
    widget = make_widget()

    dialog = UIDialog(
        id="dialog-test",
        name="Test Dialog",
    )

    ui_dialog_manager.register(
        dialog
    )

    widget.action_type = (
        ActionType.OPEN_DIALOG
    )

    widget.action = {
        "dialog_id": (
            "dialog-test"
        ),
    }

    result = (
        ui_action_executor.execute(
            widget
        )
    )

    assert result[
        "executed"
    ] is True

    assert dialog.visible is True

    widget.action_type = (
        ActionType.CLOSE_DIALOG
    )

    widget.action = {
        "dialog_id": (
            "dialog-test"
        ),
    }

    result = (
        ui_action_executor.execute(
            widget
        )
    )

    assert result[
        "executed"
    ] is True

    assert dialog.visible is False

    ui_dialog_manager.remove(
        "dialog-test"
    )


def test_automation_action_does_not_bypass_runtime():
    widget = make_widget()

    widget.action_type = (
        ActionType.AUTOMATION
    )

    widget.action = {
        "command": "start_motor",
    }

    result = (
        ui_action_executor.execute(
            widget
        )
    )

    assert result[
        "executed"
    ] is False

    assert result[
        "reason"
    ] == "runtime_bridge_required"
