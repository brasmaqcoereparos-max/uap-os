from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


VALID_WORKSPACE_LEVELS = {
    "beginner",
    "intermediate",
    "professional",
}


@dataclass
class UIWorkspace:
    id: str
    name: str

    active_screen_id: (
        str | None
    ) = None

    active_panel_id: (
        str | None
    ) = None

    zoom: float = 1.0

    readonly: bool = False

    user_level: str = "beginner"

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        self.set_user_level(
            self.user_level
        )

    def activate_screen(
        self,
        screen_id: str | None,
    ):
        self.active_screen_id = (
            screen_id
        )

        return screen_id

    def activate_panel(
        self,
        panel_id: str | None,
    ):
        self.active_panel_id = (
            panel_id
        )

        return panel_id

    def set_zoom(
        self,
        value: float,
    ):
        self.zoom = max(
            0.1,
            min(
                5.0,
                float(value),
            ),
        )

        return self.zoom

    def set_user_level(
        self,
        level: str,
    ) -> str:
        normalized = str(
            level
        ).strip().lower()

        if normalized not in VALID_WORKSPACE_LEVELS:
            raise ValueError(
                f"Unsupported workspace level: {level}"
            )

        self.user_level = normalized

        return self.user_level

    def set_readonly(
        self,
        readonly: bool,
    ) -> bool:
        self.readonly = bool(
            readonly
        )

        return self.readonly

    def can_edit(self) -> bool:
        return not self.readonly

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "active_screen_id": (
                self.active_screen_id
            ),
            "active_panel_id": (
                self.active_panel_id
            ),
            "zoom": self.zoom,
            "readonly": (
                self.readonly
            ),
            "user_level": (
                self.user_level
            ),
            "metadata": dict(
                self.metadata
            ),
                }
