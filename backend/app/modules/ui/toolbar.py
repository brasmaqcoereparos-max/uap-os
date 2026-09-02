from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIToolbarItem:
    id: str
    command: str

    label: str = ""
    icon: str | None = None

    order: int = 0

    enabled: bool = True
    visible: bool = True

    parameters: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "command": self.command,
            "label": self.label,
            "icon": self.icon,
            "order": self.order,
            "enabled": self.enabled,
            "visible": self.visible,
            "parameters": dict(
                self.parameters
            ),
        }


class UIToolbar:

    def __init__(self):
        self._items: dict[
            str,
            UIToolbarItem,
        ] = {}

    def register(
        self,
        item: UIToolbarItem,
    ):
        self._items[
            item.id
        ] = item

        return item

    def get(
        self,
        item_id: str,
    ):
        return self._items.get(
            item_id
        )

    def remove(
        self,
        item_id: str,
    ):
        return self._items.pop(
            item_id,
            None,
        )

    def list_all(
        self,
        visible_only: bool = True,
    ):
        items = list(
            self._items.values()
        )

        if visible_only:
            items = [
                item
                for item in items
                if item.visible
            ]

        return sorted(
            items,
            key=lambda item: (
                item.order,
                item.id,
            ),
        )


ui_toolbar = UIToolbar()
