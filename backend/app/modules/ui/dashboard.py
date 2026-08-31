from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIDashboardItem:
    id: str
    name: str

    item_type: str

    source_key: str | None = None

    x: int = 0
    y: int = 0

    width: int = 1
    height: int = 1

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "item_type": (
                self.item_type
            ),
            "source_key": (
                self.source_key
            ),
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "properties": dict(
                self.properties
            ),
        }


@dataclass
class UIDashboard:
    id: str
    name: str

    columns: int = 12

    items: list[
        UIDashboardItem
    ] = field(
        default_factory=list
    )

    def add(
        self,
        item: UIDashboardItem,
    ):
        if self.get(item.id):
            raise ValueError(
                "Dashboard item already "
                f"exists: {item.id}"
            )

        self.items.append(item)

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
        item = self.get(item_id)

        if not item:
            return False

        self.items.remove(item)

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "columns": self.columns,
            "items": [
                item.to_dict()
                for item in self.items
            ],
        }
