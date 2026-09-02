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
            )
        )

    def profiles(self):
        return [
            profile.to_dict()
            for profile
            in ui_device_profiles
            .list_all()
        ]


ui_studio_preview_service = (
    UIStudioPreviewService()
)
