from app.modules.ui.enums import (
    WidgetType,
)
from app.modules.ui.palette_category import (
    UIPaletteCategory,
)
from app.modules.ui.palette_item import (
    UIPaletteItem,
)
from app.modules.ui.palette_registry import (
    ui_palette_registry,
)


class UIPaletteDefaults:

    @staticmethod
    def install():
        categories = [
            UIPaletteCategory(
                id="basic",
                name="Basic",
                order=10,
            ),
            UIPaletteCategory(
                id="input",
                name="Input",
                order=20,
            ),
            UIPaletteCategory(
                id="data",
                name="Data",
                order=30,
            ),
            UIPaletteCategory(
                id="media",
                name="Media",
                order=40,
            ),
            UIPaletteCategory(
                id="layout",
                name="Layout",
                order=50,
            ),
        ]

        for category in categories:
            ui_palette_registry.register_category(
                category
            )

        definitions = [
            (
                "text",
                "Text",
                WidgetType.TEXT,
                "basic",
            ),
            (
                "button",
                "Button",
                WidgetType.BUTTON,
                "basic",
            ),
            (
                "icon",
                "Icon",
                WidgetType.ICON,
                "basic",
            ),
            (
                "input",
                "Input",
                WidgetType.INPUT,
                "input",
            ),
            (
                "switch",
                "Switch",
                WidgetType.SWITCH,
                "input",
            ),
            (
                "slider",
                "Slider",
                WidgetType.SLIDER,
                "input",
            ),
            (
                "gauge",
                "Gauge",
                WidgetType.GAUGE,
                "data",
            ),
            (
                "indicator",
                "Indicator",
                WidgetType.INDICATOR,
                "data",
            ),
            (
                "chart",
                "Chart",
                WidgetType.CHART,
                "data",
            ),
            (
                "timer",
                "Timer",
                WidgetType.TIMER,
                "data",
            ),
            (
                "image",
                "Image",
                WidgetType.IMAGE,
                "media",
            ),
            (
                "video",
                "Video",
                WidgetType.VIDEO,
                "media",
            ),
            (
                "container",
                "Container",
                WidgetType.CONTAINER,
                "layout",
            ),
            (
                "custom",
                "Custom",
                WidgetType.CUSTOM,
                "basic",
            ),
        ]

        for (
            item_id,
            name,
            widget_type,
            category,
        ) in definitions:
            ui_palette_registry.register_item(
                UIPaletteItem(
                    id=item_id,
                    name=name,
                    widget_type=widget_type,
                    category=category,
                )
            )

        return ui_palette_registry


def install_default_palette():
    return UIPaletteDefaults.install()
