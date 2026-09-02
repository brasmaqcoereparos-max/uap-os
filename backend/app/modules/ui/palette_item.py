from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.enums import (
    WidgetType,
)


@dataclass
class UIPaletteItem:
    id: str
    name: str

    widget_type: WidgetType

    category: str = "general"

    description: str = ""

    icon: str | None = None

    tags: list[str] = field(
        default_factory=list
    )

    default_properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    enabled: bool = True

    def matches(
        self,
        query: str,
    ):
        query = query.strip().lower()

        if not query:
            return True

        if query in self.name.lower():
            return True

        if (
            query
            in self.description.lower()
        ):
            return True

        if (
            query
            in self.category.lower()
        ):
            return True

        return any(
            query in tag.lower()
            for tag in self.tags
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "widget_type": (
                self.widget_type.value
            ),
            "category": self.category,
            "description": (
                self.description
            ),
            "icon": self.icon,
            "tags": list(self.tags),
            "default_properties": dict(
                self.default_properties
            ),
            "enabled": self.enabled,
  }
