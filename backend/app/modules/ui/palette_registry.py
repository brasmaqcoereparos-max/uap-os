from app.modules.ui.palette_category import (
    UIPaletteCategory,
)
from app.modules.ui.palette_item import (
    UIPaletteItem,
)


class UIPaletteRegistry:

    def __init__(self):
        self._items: dict[
            str,
            UIPaletteItem,
        ] = {}

        self._categories: dict[
            str,
            UIPaletteCategory,
        ] = {}

    def register_item(
        self,
        item: UIPaletteItem,
    ):
        self._items[
            item.id
        ] = item

        return item

    def get_item(
        self,
        item_id: str,
    ):
        return self._items.get(
            item_id
        )

    def remove_item(
        self,
        item_id: str,
    ):
        return self._items.pop(
            item_id,
            None,
        )

    def register_category(
        self,
        category: UIPaletteCategory,
    ):
        self._categories[
            category.id
        ] = category

        return category

    def get_category(
        self,
        category_id: str,
    ):
        return self._categories.get(
            category_id
        )

    def categories(self):
        return sorted(
            (
                category
                for category
                in self._categories.values()
                if category.enabled
            ),
            key=lambda category: (
                category.order,
                category.name,
            ),
        )

    def items(
        self,
        category: str | None = None,
    ):
        result = [
            item
            for item
            in self._items.values()
            if item.enabled
        ]

        if category is not None:
            result = [
                item
                for item in result
                if (
                    item.category
                    == category
                )
            ]

        return sorted(
            result,
            key=lambda item: (
                item.category,
                item.name,
            ),
        )

    def search(
        self,
        query: str,
    ):
        return [
            item
            for item in self.items()
            if item.matches(query)
        ]

    def clear(self):
        self._items.clear()
        self._categories.clear()


ui_palette_registry = (
    UIPaletteRegistry()
  )
