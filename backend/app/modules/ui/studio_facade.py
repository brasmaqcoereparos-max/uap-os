from __future__ import annotations

from app.modules.ui.hierarchy_service import (
    ui_hierarchy_service,
)
from app.modules.ui.palette_service import (
    ui_palette_service,
)
from app.modules.ui.preview_service import (
    ui_studio_preview_service,
)
from app.modules.ui.property_inspector import (
    ui_property_inspector,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.studio_service import (
    ui_studio_service,
)
from app.modules.ui.studio_state import (
    ui_studio_state,
)


class UIStudioFacade:

    def initialize(
        self,
        user_level: str | None = None,
    ):
        return (
            ui_studio_service
            .initialize(
                user_level=user_level
            )
        )

    def snapshot(self):
        return {
            "studio": (
                ui_studio_service
                .snapshot()
            ),
            "state": (
                ui_studio_state
                .to_dict()
            ),
        }

    def set_user_level(
        self,
        level: str,
    ):
        return (
            ui_studio_service
            .set_user_level(
                level
            )
        )

    def user_level(self):
        return (
            ui_studio_service
            .user_level()
        )

    def capabilities(self):
        return dict(
            ui_studio_service
            .policy()
            .capabilities
        )

    def capability(
        self,
        name: str,
    ) -> bool:
        return (
            ui_studio_service
            .capability(
                name
            )
        )

    def select_screen(
        self,
        screen_id: str,
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

        ui_studio_state.select_screen(
            screen_id
        )

        return screen

    def select_widget(
        self,
        screen_id: str,
        widget_id: str,
    ):
        screen = (
            ui_registry.get_screen(
                screen_id
            )
        )

        if (
            not screen
            or not screen.layout
        ):
            raise ValueError(
                "Screen not found"
            )

        widget = (
            screen.layout
            .get_widget(
                widget_id
            )
        )

        if not widget:
            raise ValueError(
                "Widget not found"
            )

        ui_studio_state.select_screen(
            screen_id
        )

        ui_studio_state.select_widget(
            widget_id
        )

        return {
            "widget": (
                widget.to_dict()
            ),
            "properties": (
                ui_property_inspector
                .inspect_widget(
                    widget
                )
            ),
        }

    def hierarchy(
        self,
        screen_id: str,
    ):
        if not self.capability(
            "hierarchy"
        ):
            raise PermissionError(
                "Hierarchy is not available "
                "for the current user level"
            )

        return (
            ui_hierarchy_service
            .snapshot(
                screen_id
            )
        )

    def palette(
        self,
        category: (
            str | None
        ) = None,
    ):
        return (
            ui_palette_service
            .items(
                category
            )
        )

    def preview(
        self,
        screen_id: str,
        profile_id: str = "desktop",
    ):
        if not self.capability(
            "preview"
        ):
            raise PermissionError(
                "Preview is not available "
                "for the current user level"
            )

        ui_studio_state.set_preview_profile(
            profile_id
        )

        ui_studio_state.enable_preview(
            profile_id
        )

        return (
            ui_studio_preview_service
            .preview(
                screen_id,
                profile_id,
            )
        )


ui_studio_facade = (
    UIStudioFacade()
            )
