from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIStatusItem:
    id: str
    text: str

    priority: int = 0

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "priority": (
                self.priority
            ),
            "metadata": dict(
                self.metadata
            ),
        }


class UIStatusBar:

    def __init__(self):
        self._items: dict[
            str,
            UIStatusItem,
        ] = {}

    def set(
        self,
        item_id: str,
        text: str,
        priority: int = 0,
        metadata: dict | None = None,
    ):
        item = UIStatusItem(
            id=item_id,
            text=text,
            priority=priority,
            metadata=dict(
                metadata or {}
            ),
        )

        self._items[
            item_id
        ] = item

        return item

    def remove(
        self,
        item_id: str,
    ):
        return self._items.pop(
            item_id,
            None,
        )

    def list_all(self):
        return sorted(
            self._items.values(),
            key=lambda item: (
                item.priority,
                item.id,
            ),
        )

    def to_dict(self):
        return [
            item.to_dict()
            for item
            in self.list_all()
        ]


ui_status_bar = UIStatusBar()
