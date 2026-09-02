from app.modules.ui.context_menu import (
    UIContextMenu,
)
from app.modules.ui.context_menu_item import (
    UIContextMenuItem,
)
from app.modules.ui.context_menu_registry import (
    ui_context_menu_registry,
)


class UIContextMenuDefaults:

    @staticmethod
    def install():
        widget_menu = UIContextMenu(
            id="widget",
            name="Widget",
        )

        definitions = [
            (
                "duplicate",
                "Duplicate",
                "ui.duplicate",
                10,
            ),
            (
                "rename",
                "Rename",
                "ui.rename",
                20,
            ),
            (
                "separator-1",
                "",
                None,
                30,
            ),
            (
                "show",
                "Show",
                "ui.show",
                40,
            ),
            (
                "hide",
                "Hide",
                "ui.hide",
                50,
            ),
            (
                "lock",
                "Lock",
                "ui.lock",
                60,
            ),
            (
                "unlock",
                "Unlock",
                "ui.unlock",
                70,
            ),
            (
                "separator-2",
                "",
                None,
                80,
            ),
            (
                "delete",
                "Delete",
                "ui.delete",
                90,
            ),
        ]

        for (
            item_id,
            label,
            command,
            order,
        ) in definitions:
            widget_menu.add(
                UIContextMenuItem(
                    id=item_id,
                    label=label,
                    command=command,
                    separator=(
                        command is None
                    ),
                    order=order,
                )
            )

        ui_context_menu_registry.register(
            widget_menu
        )

        return widget_menu


def install_default_context_menus():
    return (
        UIContextMenuDefaults
        .install()
    )
