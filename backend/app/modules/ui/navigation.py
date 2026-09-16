from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


VALID_PANEL_POSITIONS = {
    "left",
    "right",
    "top",
    "bottom",
    "center",
}


@dataclass
class UIPanel:
    id: str
    name: str

    title: str = ""

    position: str = "left"

    width: float = 280
    height: float | None = None

    visible: bool = True
    collapsed: bool = False
    resizable: bool = True

    order: int = 0

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        if (
            self.position
            not in VALID_PANEL_POSITIONS
        ):
            raise ValueError(
                "Invalid panel position: "
                f"{self.position}"
            )

        self.width = max(
            1.0,
            float(self.width),
        )

        if self.height is not None:
            self.height = max(
                1.0,
                float(self.height),
            )

        self.order = int(
            self.order
        )

    def show(self):
        self.visible = True
        return self

    def hide(self):
        self.visible = False
        return self

    def toggle_visibility(self):
        self.visible = not self.visible
        return self.visible

    def collapse(self):
        self.collapsed = True
        return self

    def expand(self):
        self.collapsed = False
        return self

    def toggle_collapsed(self):
        self.collapsed = (
            not self.collapsed
        )

        return self.collapsed

    def set_position(
        self,
        position: str,
    ) -> str:
        if (
            position
            not in VALID_PANEL_POSITIONS
        ):
            raise ValueError(
                "Invalid panel position: "
                f"{position}"
            )

        self.position = position

        return self.position

    def resize(
        self,
        width: float | None = None,
        height: float | None = None,
    ):
        if not self.resizable:
            return False

        if width is not None:
            self.width = max(
                1.0,
                float(width),
            )

        if height is not None:
            self.height = max(
                1.0,
                float(height),
            )

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": (
                self.title
                or self.name
            ),
            "position": self.position,
            "width": self.width,
            "height": self.height,
            "visible": self.visible,
            "collapsed": (
                self.collapsed
            ),
            "resizable": (
                self.resizable
            ),
            "order": self.order,
            "metadata": dict(
                self.metadata
            ),
        }
