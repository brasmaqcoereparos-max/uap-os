from app.modules.ui.enums import (
    ActionType,
    ScreenType,
    WidgetType,
)
from app.modules.ui.event import (
    UIEvent,
)
from app.modules.ui.event_bus import (
    ui_event_bus,
)
from app.modules.ui.facade import (
    ui_facade,
)
from app.modules.ui.runtime_bridge import (
    ui_runtime_bridge,
)
from app.modules.ui.service import (
    UIService,
)


def test_ui_facade_creates_screen():
    screen = ui_facade.create_screen(
        name="boundary-screen",
        title="Boundary Screen",
        route="/boundary",
        screen_type=ScreenType.STANDARD,
    )

    assert screen is not None
    assert screen.name == (
        "boundary-screen"
    )


def test_ui_facade_adds_widget():
    screen = ui_facade.create_screen(
        name="boundary-widget-screen",
        title="Boundary Widget",
        route="/boundary-widget",
        screen_type=ScreenType.STANDARD,
    )

    widget = ui_facade.add_widget(
        screen_id=screen.id,
        name="boundary-button",
        widget_type=WidgetType.BUTTON,
    )

    assert widget is not None
    assert widget.name == (
        "boundary-button"
    )

    assert (
        widget.widget_type
        == WidgetType.BUTTON
    )


def test_ui_action_configuration():
    screen = UIService.create_screen(
        name="action-screen",
        title="Action Screen",
        route="/action",
        screen_type=ScreenType.STANDARD,
    )

    widget = UIService.add_widget(
        screen_id=screen.id,
        name="action-button",
        widget_type=WidgetType.BUTTON,
    )

    configured = (
        UIService.configure_action(
            screen_id=screen.id,
            widget_id=widget.id,
            action_type=(
                ActionType.COMMAND
            ),
            action={
                "command": (
                    "application.test"
                ),
                "parameters": {
                    "source": "ui"
                },
            },
        )
    )

    assert configured is widget

    assert (
        configured.action_type
        == ActionType.COMMAND
    )

    assert configured.action[
        "command"
    ] == "application.test"


def test_runtime_bridge_state_update():
    key = "boundary.test"

    result = (
        ui_runtime_bridge
        .update_state(
            key,
            True,
        )
    )

    assert result is True

    snapshot = (
        ui_runtime_bridge
        .snapshot()
    )

    assert isinstance(
        snapshot,
        dict,
    )


def test_ui_facade_state_update():
    result = (
        ui_facade.update_state(
            "boundary.facade",
            "ready",
        )
    )

    assert result == "ready"


def test_ui_event_contract():
    event = UIEvent(
        event_type="command",
        source="ui",
        data={
            "command": (
                "application.test"
            ),
            "parameters": {
                "source": "boundary"
            },
        },
    )

    assert (
        event.event_type
        == "command"
    )

    assert event.source == "ui"

    assert event.data[
        "command"
    ] == "application.test"


def test_ui_event_bus_available():
    assert ui_event_bus is not None


def test_ui_does_not_require_direct_gpio():
    screen = UIService.create_screen(
        name="safe-boundary-screen",
        title="Safe Boundary",
        route="/safe-boundary",
        screen_type=ScreenType.STANDARD,
    )

    widget = UIService.add_widget(
        screen_id=screen.id,
        name="safe-button",
        widget_type=WidgetType.BUTTON,
    )

    configured = (
        UIService.configure_action(
            screen_id=screen.id,
            widget_id=widget.id,
            action_type=(
                ActionType.COMMAND
            ),
            action={
                "command": (
                    "device.request"
                ),
                "parameters": {
                    "device_id": (
                        "virtual-device"
                    ),
                    "operation": (
                        "activate"
                    ),
                },
            },
        )
    )

    assert configured.action[
        "command"
    ] == "device.request"

    assert (
        "gpio"
        not in configured.action
    )


def test_voice_ready_command_contract():
    command = {
        "command": (
            "ui.navigate"
        ),
        "parameters": {
            "route": "/home"
        },
        "source": "voice",
    }

    assert (
        command["command"]
        == "ui.navigate"
    )

    assert (
        command["source"]
        == "voice"
    )

    assert (
        command["parameters"][
            "route"
        ]
        == "/home"
    )


def test_ui_boundary_ready():
    health = (
        ui_facade.health()
    )

    assert isinstance(
        health,
        dict,
  )
