from app.modules.ui.enums import (
    ActionType,
    LayoutType,
    ScreenType,
    WidgetType,
)
from app.modules.ui.layout import (
    UILayout,
)
from app.modules.ui.persistence import (
    UIPersistence,
)
from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.serializer import (
    UISerializer,
)
from app.modules.ui.theme import (
    UITheme,
)
from app.modules.ui.widget import (
    UIWidget,
)


def build_screen():
    layout = UILayout(
        id="layout-main",
        name="Main Layout",
        layout_type=LayoutType.FREE,
        width=1280,
        height=720,
        gap=8,
        padding=12,
    )

    button = UIWidget(
        id="button-start",
        name="Start",
        widget_type=WidgetType.BUTTON,
        x=100,
        y=150,
        width=180,
        height=60,
        properties={
            "text": "Start",
        },
        style={
            "font_size": 18,
        },
        action_type=(
            ActionType.AUTOMATION
        ),
        action={
            "runtime_action": "start",
        },
    )

    layout.add_widget(
        button
    )

    return UIScreen(
        id="screen-main",
        name="Main",
        title="Main Screen",
        screen_type=(
            ScreenType.CONTROL
        ),
        route="/main",
        layout=layout,
        visible=True,
        enabled=True,
        metadata={
            "source": "test",
        },
    )


def test_screen_serialization_roundtrip():
    screen = build_screen()

    data = (
        UISerializer
        .screen_to_dict(
            screen
        )
    )

    restored = (
        UISerializer
        .screen_from_dict(
            data
        )
    )

    assert restored.id == screen.id
    assert restored.name == screen.name
    assert restored.route == "/main"

    assert (
        restored.screen_type
        == ScreenType.CONTROL
    )

    assert restored.layout is not None

    assert (
        restored.layout.layout_type
        == LayoutType.FREE
    )

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
        widget.widget_type
        == WidgetType.BUTTON
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


def test_screen_json_roundtrip():
    screen = build_screen()

    payload = (
        UISerializer
        .screen_to_json(
            screen
        )
    )

    restored = (
        UISerializer
        .screen_from_json(
            payload
        )
    )

    assert (
        restored.to_dict()
        == screen.to_dict()
    )


def test_theme_roundtrip():
    theme = UITheme(
        id="theme-main",
        name="Main Theme",
        mode="dark",
        primary_color="#123456",
    )

    payload = (
        UISerializer
        .theme_to_json(
            theme
        )
    )

    restored = (
        UISerializer
        .theme_from_json(
            payload
        )
    )

    assert restored.id == theme.id
    assert restored.name == theme.name
    assert restored.mode == "dark"

    assert (
        restored.primary_color
        == "#123456"
    )


def test_screen_persistence(
    tmp_path,
):
    persistence = UIPersistence(
        tmp_path
    )

    screen = build_screen()

    path = (
        persistence.save_screen(
            "main-screen",
            screen,
        )
    )

    assert path.exists()

    restored = (
        persistence.load_screen(
            "main-screen"
        )
    )

    assert restored is not None

    assert (
        restored.to_dict()
        == screen.to_dict()
    )


def test_theme_persistence(
    tmp_path,
):
    persistence = UIPersistence(
        tmp_path
    )

    theme = UITheme(
        id="theme-1",
        name="Theme",
        mode="light",
    )

    persistence.save_theme(
        "theme",
        theme,
    )

    restored = (
        persistence.load_theme(
            "theme"
        )
    )

    assert restored is not None
    assert restored.id == "theme-1"


def test_persistence_list_and_delete(
    tmp_path,
):
    persistence = UIPersistence(
        tmp_path
    )

    persistence.save(
        "project-a",
        {
            "value": 1,
        },
    )

    assert (
        persistence.exists(
            "project-a"
        )
        is True
    )

    assert (
        "project-a.json"
        in persistence.list_files()
    )

    assert (
        persistence.delete(
            "project-a"
        )
        is True
    )

    assert (
        persistence.exists(
            "project-a"
        )
        is False
    )


def test_missing_persistence_returns_none(
    tmp_path,
):
    persistence = UIPersistence(
        tmp_path
    )

    assert (
        persistence.load_screen(
            "missing"
        )
        is None
    )
