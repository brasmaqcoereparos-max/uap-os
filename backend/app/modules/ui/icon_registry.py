from app.modules.ui.icon import (
    UIIcon,
)


class UIIconRegistry:

    def __init__(self):
        self._icons: dict[
            str,
            UIIcon,
        ] = {}

    def register(
        self,
        icon: UIIcon,
    ):
        self._icons[
            icon.id
        ] = icon

        return icon

    def get(
        self,
        icon_id: str,
    ):
        return self._icons.get(
            icon_id
        )

    def remove(
        self,
        icon_id: str,
    ):
        return self._icons.pop(
            icon_id,
            None,
        )

    def search(
        self,
        query: str,
    ):
        return [
            icon
            for icon
            in self._icons.values()
            if icon.matches(query)
        ]

    def list_all(self):
        return list(
            self._icons.values()
        )

    def clear(self):
        self._icons.clear()


ui_icon_registry = (
    UIIconRegistry()
)
