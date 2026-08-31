import uuid
from typing import Any

from app.modules.ui.enums import (
    WidgetType,
)
from app.modules.ui.widget import (
    UIWidget,
)


class UIWidgetFactory:

    @staticmethod
    def create(
        widget_type: WidgetType,
        name: str | None = None,
        properties: (
            dict[str, Any] | None
        ) = None,
    ):
        widget_id = str(
            uuid.uuid4()
        )

        if name is None:
            name = (
                widget_type.value
                .replace("_", " ")
                .title()
            )

        widget = UIWidget(
            id=widget_id,
            name=name,
            widget_type=widget_type,
            properties=(
                dict(properties)
                if properties
                else {}
            ),
        )

        UIWidgetFactory.apply_defaults(
            widget
        )

        return widget

    @staticmethod
    def apply_defaults(
        widget: UIWidget,
    ):
        defaults = {
            WidgetType.TEXT: (
                160,
                32,
            ),
            WidgetType.BUTTON: (
                140,
                44,
            ),
            WidgetType.IMAGE: (
                160,
                120,
            ),
            WidgetType.ICON: (
                48,
                48,
            ),
            WidgetType.INPUT: (
                200,
                44,
            ),
            WidgetType.SWITCH: (
                64,
                32,
            ),
            WidgetType.SLIDER: (
                200,
                40,
            ),
            WidgetType.GAUGE: (
                160,
                160,
            ),
            WidgetType.INDICATOR: (
                48,
                48,
            ),
            WidgetType.CHART: (
                320,
                200,
            ),
            WidgetType.TIMER: (
                160,
                64,
            ),
            WidgetType.VIDEO: (
                320,
                180,
            ),
            WidgetType.CONTAINER: (
                300,
                200,
            ),
            WidgetType.CUSTOM: (
                160,
                100,
            ),
        }

        size = defaults.get(
            widget.widget_type,
            (
                100,
                40,
            ),
        )

        widget.width = size[0]
        widget.height = size[1]

        return widget
