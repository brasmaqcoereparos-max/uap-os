import pytest

from app.modules.runtime.runtime_context import (
    RuntimeContext,
)
from app.modules.ui.enums import (
    ActionType,
    LayoutType,
    ScreenType,
    WidgetType,
)
from app.modules.ui.layout import (
    UILayout,
)
from app.modules.ui.preview_service import (
    UIStudioPreviewService,
)
from app.modules.ui.registry import (
    UIRegistry,
)
from app.modules.ui.runtime_bridge import (
    UIRuntimeBridge,
)
from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.serializer import (
    UISerializer,
)
from app.modules.ui.studio_level_policy import (
    get_studio_level_policy,
)
from app.modules.ui.widget import (
    UIWidget,
)


class FakeHardware:
    def __init__(self):
        self.writes = []

    def write(
        self,
        pin,
        value,
    ):
        self.writes.append(
            (
                pin,
                value,
            )
        )

        return True

    def read(
        self,
        pin,
    ):
        return None

    def pwm(
        self,
        pin,
        duty,
    ):
        return True


def build_screen():
    layout = UILayout(
        id="layout-final",
        name="Final Layout",
        layout_type=LayoutType.FREE,
        width=1280,
        height=720,
    )

    widget = UIWidget(
        id="button-start",
        name="Start",
        widget_type=WidgetType.BUTTON,
        x=100,
        y=100,
        width=200,
        height=60,
        action_type=ActionType.AUTOMATION,
        action={
            "runtime_action": "start",
        },
    )

    layout.add_widget(
        widget
    )

    return UIScreen(
        id="screen-final",
        name="Final Screen",
        title="Final Screen",
        screen_type=ScreenType.CONTROL,
        route="/final",
        layout=layout,
    )


def test_beginner_level_hides_advanced_features():
    policy = (
        get_studio_level_policy(
            "beginner"
        )
    )

    assert (
        policy.allows(
            "visual_editor"
        )
        is True
    )

    assert (
        policy.allows(
            "advanced_properties"
        )
        is False
    )

    assert (
        policy.allows(
            "hardware_details"
        )
        is False
    )

    assert (
        policy.allows(
            "code_details"
        )
        is False
    )


def test_intermediate_level_enables_visual_controls():
    policy = (
        get_studio_level_policy(
            "intermediate"
        )
    )

    assert (
        policy.allows(
            "advanced_properties"
        )
        is True
    )

    assert (
        policy.allows(
            "events"
        )
        is True
    )

    assert (
        policy.allows(
            "hierarchy"
        )
        is True
    )


def test_professional_level_enables_advanced_features():
    policy = (
        get_studio_level_policy(
            "professional"
        )
    )

    assert (
        policy.allows(
            "hardware_details"
        )
        is True
    )

    assert (
        policy.allows(
            "code_details"
        )
        is True
    )

    assert (
        policy.allows(
            "console"
        )
        is True
    )


def test_screen_serialization_preserves_contract():
    screen = build_screen()

    serialized = (
        UISerializer
        .screen_to_dict(
            screen
        )
    )

    restored = (
        UISerializer
        .screen_from_dict(
            serialized
        )
    )

    assert restored.id == screen.id
    assert restored.route == "/final"

    assert (
        restored.screen_type
        == ScreenType.CONTROL
    )

    assert restored.layout is not None

    assert (
        len(
            restored.layout.widgets
        )
        == 1
    )

    widget = (
        restored.layout.widgets[
            0
        ]
    )

    assert (
        widget.action_type
        == ActionType.AUTOMATION
    )

    assert (
        widget.action[
            "runtime_action"
        ]
        == "start"
    )


def test_registry_preserves_screen_route_contract():
    registry = UIRegistry()

    screen = build_screen()

    registry.register_screen(
        screen
    )

    assert (
        registry.get_screen(
            screen.id
        )
        is screen
    )

    assert (
        registry.get_screen_by_route(
            "/final"
        )
        is screen
    )

    with pytest.raises(
        ValueError
    ):
        registry.register_screen(
            UIScreen(
                id="duplicate-route",
                name="Duplicate",
                route="/final",
            )
        )


def test_ui_runtime_bridge_executes_only_runtime_actions():
    runtime = RuntimeContext(
        "project-block8"
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

    assert (
        result["executed"]
        is True
    )

    assert (
        runtime.state.running
        is True
    )

    bridge.execute_runtime_action(
        "stop"
    )

    assert (
        runtime.state.running
        is False
    )

    with pytest.raises(
        ValueError
    ):
        bridge.execute_runtime_action(
            "direct_gpio_write"
        )


def test_ui_runtime_bridge_respects_interlocks():
    runtime = RuntimeContext(
        "project-block8-safety"
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


def test_ui_runtime_hardware_path():
    hardware = FakeHardware()

    runtime = RuntimeContext(
        "project-block8-hardware",
        hardware=hardware,
    )

    runtime.io.configure(
        name="relay",
        direction="output",
        data_type="bool",
        physical_port="GPIO23",
    )

    bridge = UIRuntimeBridge()

    bridge.bind_runtime(
        runtime
    )

    bridge.execute_runtime_action(
        "start"
    )

    runtime.io.write(
        "relay",
        True,
    )

    assert hardware.writes == [
        (
            "GPIO23",
            True,
        )
    ]

    bridge.execute_runtime_action(
        "stop"
    )


def test_ui_preview_boundary(
    monkeypatch,
):
    screen = build_screen()

    from app.modules.ui import (
        preview_service,
    )

    monkeypatch.setattr(
        preview_service.ui_registry,
        "get_screen",
        lambda screen_id: (
            screen
            if screen_id
            == screen.id
            else None
        ),
    )

    service = (
        UIStudioPreviewService()
    )

    preview = service.preview(
        screen_id=screen.id,
        profile_id="desktop",
    )

    assert (
        preview.screen_id
        == screen.id
    )

    assert (
        preview.profile_id
        == "desktop"
    )

    assert (
        preview.context.preview
        is True
    )


def test_block8_boundary_complete():
    screen = build_screen()

    assert screen.layout is not None

    assert (
        screen.layout.layout_type
        == LayoutType.FREE
    )

    assert (
        screen.layout.widgets[
            0
        ].widget_type
        == WidgetType.BUTTON
    )

    policy = (
        get_studio_level_policy(
            "professional"
        )
    )

    assert (
        policy.allows(
            "visual_editor"
        )
        is True
    )

    serialized = (
        UISerializer
        .screen_to_dict(
            screen
        )
    )

    assert (
        serialized["id"]
        == "screen-final"
        )
