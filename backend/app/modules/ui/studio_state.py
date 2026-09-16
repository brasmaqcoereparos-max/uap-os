from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


VALID_STUDIO_LEVELS = {
    "beginner",
    "intermediate",
    "professional",
}


@dataclass
class UIStudioState:
    active_screen_id: (
        str | None
    ) = None

    active_widget_id: (
        str | None
    ) = None

    active_tool: str = "select"

    preview_profile_id: str = "desktop"

    preview_enabled: bool = False

    user_level: str = "beginner"

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def select_screen(
        self,
        screen_id: str | None,
    ):
        self.active_screen_id = (
            screen_id
        )

        self.active_widget_id = None

        return screen_id

    def select_widget(
        self,
        widget_id: str | None,
    ):
        self.active_widget_id = (
            widget_id
        )

        return widget_id

    def set_tool(
        self,
        tool: str,
    ):
        self.active_tool = str(
            tool
        )

        return self.active_tool

    def set_preview_profile(
        self,
        profile_id: str,
    ):
        self.preview_profile_id = str(
            profile_id
        )

        return self.preview_profile_id

    def enable_preview(
        self,
        profile_id: str | None = None,
    ) -> None:
        if profile_id is not None:
            self.set_preview_profile(
                profile_id
            )

        self.preview_enabled = True

    def disable_preview(self) -> None:
        self.preview_enabled = False

    def set_user_level(
        self,
        level: str,
    ) -> str:
        normalized = str(
            level
        ).strip().lower()

        if normalized not in VALID_STUDIO_LEVELS:
            raise ValueError(
                f"Unsupported studio level: {level}"
            )

        self.user_level = normalized

        return self.user_level

    def reset_selection(self) -> None:
        self.active_screen_id = None
        self.active_widget_id = None

    def to_dict(self):
        return {
            "active_screen_id": (
                self.active_screen_id
            ),
            "active_widget_id": (
                self.active_widget_id
            ),
            "active_tool": (
                self.active_tool
            ),
            "preview_profile_id": (
                self.preview_profile_id
            ),
            "preview_enabled": (
                self.preview_enabled
            ),
            "user_level": (
                self.user_level
            ),
            "metadata": dict(
                self.metadata
            ),
        }


ui_studio_state = UIStudioState()
