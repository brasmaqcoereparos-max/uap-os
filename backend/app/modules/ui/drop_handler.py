from app.modules.ui.drop_payload import (
    UIDropPayload,
)
from app.modules.ui.grid import (
    UIGrid,
)
from app.modules.ui.palette_registry import (
    ui_palette_registry,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.widget_factory import (
    UIWidgetFactory,
)


class UIDropHandler:

    def __init__(self):
        self.grid = UIGrid()

    def handle(
        self,
        payload: UIDropPayload,
    ):
        item = (
            ui_palette_registry
            .get_item(
                payload.palette_item_id
            )
        )

        if not item:
            raise ValueError(
                "Palette item not found: "
                f"{payload.palette_item_id}"
            )

        screen = (
            ui_registry.get_screen(
                payload.screen_id
            )
        )

        if (
            not screen
            or not screen.layout
        ):
            raise ValueError(
                "Screen not found"
            )

        properties = dict(
            item.default_properties
        )

        properties.update(
            payload.properties
        )

        widget = (
            UIWidgetFactory.create(
                widget_type=(
                    item.widget_type
                ),
                name=item.name,
                properties=properties,
            )
        )

        x, y = self.grid.snap_point(
            payload.x,
            payload.y,
        )

        widget.x = x
        widget.y = y

        screen.layout.add_widget(
            widget
        )

        return widget


ui_drop_handler = UIDropHandler()
