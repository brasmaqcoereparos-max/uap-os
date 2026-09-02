from copy import deepcopy

from app.modules.ui.component import (
    UIComponent,
)
from app.modules.ui.layout import (
    UILayout,
)
from app.modules.ui.widget import (
    UIWidget,
)


class UIComposition:

    @staticmethod
    def add_component(
        layout: UILayout,
        component: UIComponent,
        offset_x: float = 0,
        offset_y: float = 0,
    ):
        created = []

        existing_ids = {
            widget.id
            for widget in layout.widgets
        }

        for source in component.widgets:
            widget = deepcopy(source)

            base_id = widget.id
            candidate = base_id
            index = 1

            while candidate in existing_ids:
                candidate = (
                    f"{base_id}_{index}"
                )
                index += 1

            widget.id = candidate

            widget.x += offset_x
            widget.y += offset_y

            layout.add_widget(widget)

            existing_ids.add(
                widget.id
            )

            created.append(widget)

        return created

    @staticmethod
    def group_bounds(
        widgets: list[UIWidget],
    ):
        if not widgets:
            return None

        left = min(
            widget.x
            for widget in widgets
        )

        top = min(
            widget.y
            for widget in widgets
        )

        right = max(
            widget.x + widget.width
            for widget in widgets
        )

        bottom = max(
            widget.y + widget.height
            for widget in widgets
        )

        return {
            "x": left,
            "y": top,
            "width": right - left,
            "height": bottom - top,
      }
