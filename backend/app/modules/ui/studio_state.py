from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIStudioState:
    active_screen_id: (
        str | None
    ) = None

    active_widget_id: (
        str | None
    ) = None

    active_tool: str = "select"

    preview_profile_id: (
        str
    ) = "desktop"

    preview_enabled: bool = False

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
        self.active_tool = tool

        return tool

    def set_preview_profile(
        self,
        profile_id: str,
    ):
        self.preview_profile_id = (
            profile_id
        )

        return profile_id

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
            "metadata": dict(
                self.metadata
            ),
        }


ui_studio_state = UIStudioState()
