from app.modules.ui.accessibility import (
    UIAccessibility,
)


class UIAccessibilityRegistry:

    def __init__(self):
        self._items: dict[
            str,
            UIAccessibility,
        ] = {}

    def set(
        self,
        widget_id: str,
        accessibility: (
            UIAccessibility
        ),
    ):
        self._items[
            widget_id
        ] = accessibility

        return accessibility

    def get(
        self,
        widget_id: str,
    ):
        return self._items.get(
            widget_id
        )

    def remove(
        self,
        widget_id: str,
    ):
        return self._items.pop(
            widget_id,
            None,
        )

    def clear(self):
        self._items.clear()

    def to_dict(self):
        return {
            widget_id: (
                accessibility.to_dict()
            )
            for (
                widget_id,
                accessibility,
            )
            in self._items.items()
        }


ui_accessibility_registry = (
    UIAccessibilityRegistry()
)
