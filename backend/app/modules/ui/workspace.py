from dataclasses import dataclass
from dataclasses import field
from typing import Any


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

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
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
            "metadata": dict(
                self.metadata
            ),
        }
