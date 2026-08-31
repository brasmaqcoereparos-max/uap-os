import uuid

from app.modules.ui.enums import (
    LayoutType,
    ScreenType,
    WidgetType,
)
from app.modules.ui.layout import (
    UILayout,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.theme import (
    UITheme,
)
from app.modules.ui.widget import (
    UIWidget,
)


class UIService:

    @staticmethod
    def create_screen(
        name: str,
        title: str = "",
        route: str = "/",
        screen_type: ScreenType = (
            ScreenType.STANDARD
        ),
    ):
        screen_id = str(
            uuid.uuid4()
        )

        layout = UILayout(
            id=str(uuid.uuid4()),
            name=f"{name} Layout",
            layout_type=LayoutType.FREE,
        )

        screen = UIScreen(
            id=screen_id,
            name=name,
            title=title,
            route=route,
            screen_type=screen_type,
            layout=layout,
        )

        return ui_registry.register_screen(
            screen
        )

    @staticmethod
    def get_screen(
        screen_id: str,
    ):
        return ui_registry.get_screen(
            screen_id
        )

    @staticmethod
    def list_screens():
        return ui_registry.list_screens()

    @staticmethod
    def delete_screen(
        screen_id: str,
    ):
        return (
            ui_registry.remove_screen(
                screen_id
            )
            is not None
        )

    @staticmethod
    def add_widget(
        screen_id: str,
        name: str,
        widget_type: WidgetType,
    ):
        screen = (
            ui_registry.get_screen(
                screen_id
            )
        )

        if not screen:
            raise ValueError(
                "Screen not found"
            )

        if not screen.layout:
            raise ValueError(
                "Screen has no layout"
            )

        widget = UIWidget(
            id=str(uuid.uuid4()),
            name=name,
            widget_type=widget_type,
        )

        screen.layout.add_widget(
            widget
        )

        return widget

    @staticmethod
    def create_theme(
        name: str,
        mode: str = "light",
    ):
        theme = UITheme(
            id=str(uuid.uuid4()),
            name=name,
            mode=mode,
        )

        return ui_registry.register_theme(
            theme
        )

    @staticmethod
    def list_themes():
        return ui_registry.list_themes()
