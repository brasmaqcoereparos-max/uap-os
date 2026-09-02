from app.modules.ui.context_menu import (
    UIContextMenu,
)


class UIContextMenuRegistry:

    def __init__(self):
        self._menus: dict[
            str,
            UIContextMenu,
        ] = {}

    def register(
        self,
        menu: UIContextMenu,
    ):
        self._menus[
            menu.id
        ] = menu

        return menu

    def get(
        self,
        menu_id: str,
    ):
        return self._menus.get(
            menu_id
        )

    def remove(
        self,
        menu_id: str,
    ):
        return self._menus.pop(
            menu_id,
            None,
        )

    def list_all(self):
        return list(
            self._menus.values()
        )

    def clear(self):
        self._menus.clear()


ui_context_menu_registry = (
    UIContextMenuRegistry()
)
