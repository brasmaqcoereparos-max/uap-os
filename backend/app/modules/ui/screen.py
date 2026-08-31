from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.enums import (
    ScreenType,
)
from app.modules.ui.layout import (
    UILayout,
)


@dataclass
class UIScreen:
    id: str
    name: str

    title: str = ""

    screen_type: ScreenType = (
        ScreenType.STANDARD
    )

    route: str = "/"

    layout: UILayout | None = None

    visible: bool = True

    properties: dict[str, Any] = field(
        default_factory=dict
    )

    def set_layout(
        self,
        layout: UILayout,
    ):
        self.layout = layout

        return layout

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "screen_type": (
                self.screen_type.value
            ),
            "route": self.route,
            "visible": self.visible,
            "properties": dict(
                self.properties
            ),
            "layout": (
                self.layout.to_dict()
                if self.layout
                else None
            ),
        }
