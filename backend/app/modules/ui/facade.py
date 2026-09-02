from typing import Any

from app.modules.ui.enums import (
    ScreenType,
    WidgetType,
)
from app.modules.ui.health import (
    ui_health,
)
from app.modules.ui.runtime_bridge import (
    ui_runtime_bridge,
)
from app.modules.ui.service import (
    UIService,
)
from app.modules.ui.studio_facade import (
    ui_studio_facade,
)


class UIFacade:

    def create_screen(
        self,
        name: str,
        title: str = "",
        route: str = "/",
        screen_type: (
            ScreenType
        ) = ScreenType.STANDARD,
    ):
        return UIService.create_screen(
            name=name,
            title=title,
            route=route,
            screen_type=screen_type,
        )

    def add_widget(
        self,
        screen_id: str,
        name: str,
        widget_type: WidgetType,
    ):
        return UIService.add_widget(
            screen_id=screen_id,
            name=name,
            widget_type=widget_type,
        )

    def update_state(
        self,
        key: str,
        value: Any,
    ):
        return (
            ui_runtime_bridge
            .update_state(
                key,
                value,
            )
        )

    def snapshot(self):
        return (
            ui_runtime_bridge
            .snapshot()
        )

    def health(self):
        return ui_health.check()

    def studio(self):
        return (
            ui_studio_facade
            .snapshot()
        )

    def initialize_studio(self):
        return (
            ui_studio_facade
            .initialize()
        )


ui_facade = UIFacade()
