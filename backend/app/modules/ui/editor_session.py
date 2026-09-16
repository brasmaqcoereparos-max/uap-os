from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class UIEditorSession:
    project_id: str

    screen_id: str | None = None

    zoom: float = 1.0

    viewport_x: float = 0
    viewport_y: float = 0

    dirty: bool = False

    user_level: str = "beginner"

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    opened_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def set_screen(
        self,
        screen_id: str,
    ):
        self.screen_id = screen_id
        return screen_id

    def set_zoom(
        self,
        zoom: float,
    ):
        self.zoom = max(
            0.1,
            min(
                5.0,
                float(zoom),
            ),
        )

        return self.zoom

    def zoom_in(
        self,
        step: float = 0.1,
    ) -> float:
        return self.set_zoom(
            self.zoom + step
        )

    def zoom_out(
        self,
        step: float = 0.1,
    ) -> float:
        return self.set_zoom(
            self.zoom - step
        )

    def pan(
        self,
        x: float,
        y: float,
    ):
        self.viewport_x = float(
            x
        )

        self.viewport_y = float(
            y
        )

        return (
            self.viewport_x,
            self.viewport_y,
        )

    def set_user_level(
        self,
        level: str,
    ) -> str:
        normalized = str(
            level
        ).strip().lower()

        if normalized not in {
            "beginner",
            "intermediate",
            "professional",
        }:
            raise ValueError(
                f"Unsupported editor level: {level}"
            )

        self.user_level = normalized

        return self.user_level

    def mark_dirty(self):
        self.dirty = True

    def mark_saved(self):
        self.dirty = False

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "screen_id": self.screen_id,
            "zoom": self.zoom,
            "viewport_x": (
                self.viewport_x
            ),
            "viewport_y": (
                self.viewport_y
            ),
            "dirty": self.dirty,
            "user_level": (
                self.user_level
            ),
            "metadata": dict(
                self.metadata
            ),
            "opened_at": (
                self.opened_at.isoformat()
            ),
        }
