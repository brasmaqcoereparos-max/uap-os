from app.modules.ui.enums import (
    WidgetType,
)
from app.modules.ui.palette_registry import (
    ui_palette_registry,
)


class UIWidgetCatalog:

    def list_types(self):
        return [
            {
                "id": item.id,
                "name": item.name,
                "widget_type": (
                    item.widget_type.value
                ),
                "category": (
                    item.category
                ),
                "description": (
                    item.description
                ),
                "icon": item.icon,
            }
            for item
            in ui_palette_registry.items()
        ]

    def get(
        self,
        item_id: str,
    ):
        return (
            ui_palette_registry
            .get_item(
                item_id
            )
        )

    def find_by_type(
        self,
        widget_type: WidgetType,
    ):
        return [
            item
            for item
            in ui_palette_registry.items()
            if (
                item.widget_type
                == widget_type
            )
        ]

    def search(
        self,
        query: str,
    ):
        return (
            ui_palette_registry
            .search(query)
        )


ui_widget_catalog = (
    UIWidgetCatalog()
)
