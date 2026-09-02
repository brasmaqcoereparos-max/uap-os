from app.modules.ui.menu import (
    UIMenuItem,
)


class UIMenuManager:

    def __init__(self):
        self._items: dict[
            str,
            UIMenuItem,
        ] = {}

    def register(
        self,
        item: UIMenuItem,
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

    def list_all(self):
        return sorted(
            self._items.values(),
            key=lambda item: (
                item.order,
                item.label,
            ),
        )

    def visible_items(self):
        return [
            item
            for item in self.list_all()
            if (
                item.visible
                and item.enabled
            )
        ]

    def clear(self):
        self._items.clear()


ui_menu_manager = UIMenuManager()
