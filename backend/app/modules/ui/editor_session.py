from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass
class UIEditorSession:
    project_id: str

    screen_id: str | None = None

    zoom: float = 1.0

    viewport_x: float = 0
    viewport_y: float = 0

    dirty: bool = False

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    opened_at: datetime = field(
        default_factory=datetime.utcnow
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

    def pan(
        self,
        x: float,
        y: float,
    ):
        self.viewport_x = x
        self.viewport_y = y

        return (
            self.viewport_x,
            self.viewport_y,
        )

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
            "metadata": dict(
                self.metadata
            ),
            "opened_at": (
                self.opened_at.isoformat()
            ),
      }
