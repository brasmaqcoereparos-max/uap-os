from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.enums import (
    LayoutType,
)
from app.modules.ui.widget import (
    UIWidget,
)


@dataclass
class UILayout:
    id: str
    name: str

    layout_type: LayoutType = (
        LayoutType.FREE
    )

    width: float = 1280
    height: float = 720

    gap: float = 0
    padding: float = 0

    properties: dict[str, Any] = field(
        default_factory=dict
    )

    widgets: list[UIWidget] = field(
        default_factory=list
    )

    def add_widget(
        self,
        widget: UIWidget,
    ):
        existing = self.get_widget(
            widget.id
        )

        if existing:
            raise ValueError(
                "Widget already exists: "
                f"{widget.id}"
            )

        self.widgets.append(widget)

        return widget

    def get_widget(
        self,
        widget_id: str,
    ):
        for widget in self.widgets:
            if widget.id == widget_id:
                return widget

        return None

    def remove_widget(
        self,
        widget_id: str,
    ):
        widget = self.get_widget(
            widget_id
        )

        if not widget:
            return False

        self.widgets.remove(widget)

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "layout_type": (
                self.layout_type.value
            ),
            "width": self.width,
            "height": self.height,
            "gap": self.gap,
            "padding": self.padding,
            "properties": dict(
                self.properties
            ),
            "widgets": [
                widget.to_dict()
                for widget in self.widgets
            ],
      }
