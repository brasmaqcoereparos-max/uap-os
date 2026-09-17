from __future__ import annotations

from app.modules.ui.device_profiles import (
    ui_device_profiles,
)
from app.modules.ui.preview import (
    ui_preview_service,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.render_context import (
    UIRenderContext,
)


class UIStudioPreviewService:

    def preview(
        self,
        screen_id: str,
        profile_id: str = "desktop",
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

        profile = (
            ui_device_profiles.get(
                profile_id
            )
        )

        if not profile:
            raise ValueError(
                "Device profile not found"
            )

        context = UIRenderContext(
            width=profile.width,
            height=profile.height,
            device_type=(
                profile.device_type
            ),
            scale=(
                profile.pixel_ratio
            ),
            preview=True,
        )

        return (
            ui_preview_service
            .create(
                screen=screen,
                context=context,
                profile_id=profile.id,
            )
        )

    def preview_route(
        self,
        route: str,
        profile_id: str = "desktop",
    ):
        screen = (
            ui_registry
            .get_screen_by_route(
                route
            )
        )

        if screen is None:
            raise ValueError(
                "Screen route not found: "
                f"{route}"
            )

        return self.preview(
            screen_id=screen.id,
            profile_id=profile_id,
        )

    def profiles(self):
        return [
            profile.to_dict()
            for profile
            in ui_device_profiles
            .list_all()
        ]

    def screens(self):
        return [
            screen.to_dict()
            for screen
            in ui_registry.list_screens(
                visible_only=True,
                enabled_only=True,
            )
        ]

    def snapshot(
        self,
        screen_id: str,
        profile_id: str = "desktop",
    ) -> dict:
        preview = self.preview(
            screen_id=screen_id,
            profile_id=profile_id,
        )

        return preview.to_dict()


ui_studio_preview_service = (
    UIStudioPreviewService()
        )
