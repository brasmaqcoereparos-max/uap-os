from app.modules.ui.alignment import (
    UIAlignment,
)
from app.modules.ui.distribution import (
    UIDistribution,
)
from app.modules.ui.grid import (
    UIGrid,
)
from app.modules.ui.layer_manager import (
    UILayerManager,
)
from app.modules.ui.registry import (
    UIRegistry,
    ui_registry,
)
from app.modules.ui.selection import (
    UISelection,
    ui_selection,
)


class UIEditor:

    def __init__(
        self,
        registry: UIRegistry = ui_registry,
        selection: UISelection = (
            ui_selection
        ),
    ):
        self.registry = registry
        self.selection = selection

        self.grid = UIGrid()

    def get_selected_widgets(
        self,
        screen_id: str,
    ):
        screen = self.registry.get_screen(
            screen_id
        )

        if (
            not screen
            or not screen.layout
        ):
            return []

        return [
            widget
            for widget
            in screen.layout.widgets
            if self.selection.contains(
                widget.id
            )
        ]

    def move_widget(
        self,
        screen_id: str,
        widget_id: str,
        x: float,
        y: float,
    ):
        screen = self.registry.get_screen(
            screen_id
        )

        if (
            not screen
            or not screen.layout
        ):
            raise ValueError(
                "Screen not found"
            )

        widget = screen.layout.get_widget(
            widget_id
        )

        if not widget:
            raise ValueError(
                "Widget not found"
            )

        x, y = self.grid.snap_point(
            x,
            y,
        )

        widget.x = x
        widget.y = y

        return widget

    def resize_widget(
        self,
        screen_id: str,
        widget_id: str,
        width: float,
        height: float,
    ):
        screen = self.registry.get_screen(
            screen_id
        )

        if (
            not screen
            or not screen.layout
        ):
            raise ValueError(
                "Screen not found"
            )

        widget = screen.layout.get_widget(
            widget_id
        )

        if not widget:
            raise ValueError(
                "Widget not found"
            )

        widget.width = max(
            1,
            self.grid.snap(width),
        )

        widget.height = max(
            1,
            self.grid.snap(height),
        )

        return widget

    def align(
        self,
        screen_id: str,
        mode: str,
    ):
        widgets = (
            self.get_selected_widgets(
                screen_id
            )
        )

        operations = {
            "left": UIAlignment.left,
            "right": UIAlignment.right,
            "top": UIAlignment.top,
            "bottom": (
                UIAlignment.bottom
            ),
            "center_horizontal": (
                UIAlignment
                .center_horizontal
            ),
            "center_vertical": (
                UIAlignment
                .center_vertical
            ),
        }

        operation = operations.get(
            mode
        )

        if not operation:
            raise ValueError(
                f"Invalid alignment: "
                f"{mode}"
            )

        return operation(widgets)

    def distribute(
        self,
        screen_id: str,
        mode: str,
    ):
        widgets = (
            self.get_selected_widgets(
                screen_id
            )
        )

        if mode == "horizontal":
            return (
                UIDistribution.horizontal(
                    widgets
                )
            )

        if mode == "vertical":
            return (
                UIDistribution.vertical(
                    widgets
                )
            )

        raise ValueError(
            f"Invalid distribution: "
            f"{mode}"
        )

    def bring_to_front(
        self,
        screen_id: str,
        widget_id: str,
    ):
        screen = self.registry.get_screen(
            screen_id
        )

        if (
            not screen
            or not screen.layout
        ):
            return False

        return (
            UILayerManager
            .bring_to_front(
                screen.layout,
                widget_id,
            )
        )

    def send_to_back(
        self,
        screen_id: str,
        widget_id: str,
    ):
        screen = self.registry.get_screen(
            screen_id
        )

        if (
            not screen
            or not screen.layout
        ):
            return False

        return (
            UILayerManager
            .send_to_back(
                screen.layout,
                widget_id,
            )
        )


ui_editor = UIEditor()
