from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.widget import (
    UIWidget,
)


@dataclass
class UIComponent:
    id: str
    name: str

    category: str = "general"

    widgets: list[
        UIWidget
    ] = field(
        default_factory=list
    )

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_widget(
        self,
        widget: UIWidget,
    ):
        if self.get_widget(widget.id):
            raise ValueError(
                "Component widget already "
                f"exists: {widget.id}"
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
            "category": self.category,
            "widgets": [
                widget.to_dict()
                for widget in self.widgets
            ],
            "properties": dict(
                self.properties
            ),
      }
