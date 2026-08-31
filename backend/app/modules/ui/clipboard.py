from copy import deepcopy
from typing import Any


class UIClipboard:

    def __init__(self):
        self._items: list[
            dict[str, Any]
        ] = []

    def copy(
        self,
        items: list[
            dict[str, Any]
        ],
    ):
        self._items = deepcopy(
            items
        )

        return len(self._items)

    def paste(self):
        return deepcopy(
            self._items
        )

    def clear(self):
        self._items.clear()

    def has_data(self):
        return bool(self._items)

    def count(self):
        return len(self._items)


ui_clipboard = UIClipboard()
