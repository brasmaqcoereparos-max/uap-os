from dataclasses import dataclass
from dataclasses import field

from app.modules.ui.context_menu_item import (
    UIContextMenuItem,
)


@dataclass
class UIContextMenu:
    id: str
    name: str

    items: list[
        UIContextMenuItem
    ] = field(
        default_factory=list
    )

    def add(
        self,
        item: UIContextMenuItem,
    ):
        existing = self.get(
            item.id
        )

        if existing:
            self.items.remove(
                existing
            )

        self.items.append(
            item
        )

        self.items.sort(
            key=lambda value: (
                value.order,
                value.id,
            )
        )

        return item

    def get(
        self,
        item_id: str,
    ):
        for item in self.items:
            if item.id == item_id:
                return item

        return None

    def remove(
        self,
        item_id: str,
    ):
        item = self.get(
            item_id
        )

        if not item:
            return False

        self.items.remove(
            item
        )

        return True

    def visible_items(self):
        return [
            item
            for item in self.items
            if item.visible
        ]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "items": [
                item.to_dict()
                for item
                in self.visible_items()
            ],
  }
