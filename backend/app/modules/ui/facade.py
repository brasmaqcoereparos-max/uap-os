from __future__ import annotations

from typing import Any

from app.modules.ui.enums import (
    ScreenType,
    WidgetType,
)
from app.modules.ui.health import (
    ui_health,
)
from app.modules.ui.navigation import (
    ui_navigation,
)
from app.modules.ui.preview_service import (
    ui_studio_preview_service,
)
from app.modules.ui.project_registry import (
    ui_project_registry,
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

    def get_screen(
        self,
        screen_id: str,
    ):
        return UIService.get_screen(
            screen_id
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

    def navigate(
        self,
        screen_id: str,
    ):
        screen = (
            ui_navigation.navigate(
                screen_id
            )
        )

        active_project = (
            ui_project_registry
            .active()
        )

        if active_project:
            active_project.set_active_screen(
                screen.id
            )

        return screen

    def navigate_route(
        self,
        route: str,
    ):
        screen = (
            UIService
            .get_screen_by_route(
                route
            )
        )

        if screen is None:
            raise ValueError(
                "Screen route not found: "
                f"{route}"
            )

        return self.navigate(
            screen.id
        )

    def back(self):
        screen = (
            ui_navigation.back()
        )

        active_project = (
            ui_project_registry
            .active()
        )

        if (
            screen is not None
            and active_project
        ):
            active_project.set_active_screen(
                screen.id
            )

        return screen

    def forward(self):
        screen = (
            ui_navigation.forward()
        )

        active_project = (
            ui_project_registry
            .active()
        )

        if (
            screen is not None
            and active_project
        ):
            active_project.set_active_screen(
                screen.id
            )

        return screen

    def preview(
        self,
        screen_id: str,
        profile_id: str = "desktop",
    ):
        return (
            ui_studio_preview_service
            .preview(
                screen_id=screen_id,
                profile_id=profile_id,
            )
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

    def update_runtime_status(
        self,
        status: dict[str, Any],
    ):
        return (
            ui_runtime_bridge
            .update_runtime_status(
                status
            )
        )

    def open_project(
        self,
        project_id: str,
    ):
        project = (
            ui_project_registry
            .get_or_create(
                project_id
            )
        )

        ui_project_registry.activate(
            project_id
        )

        return project

    def active_project(self):
        return (
            ui_project_registry
            .active()
        )

    def snapshot(self):
        return {
            "runtime": (
                ui_runtime_bridge
                .snapshot()
            ),
            "navigation": (
                ui_navigation
                .snapshot()
            ),
            "projects": (
                ui_project_registry
                .snapshot()
            ),
        }

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
