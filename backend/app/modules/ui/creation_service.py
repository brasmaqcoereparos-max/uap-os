from app.modules.ui.creation_request import (
    UIWidgetCreationRequest,
)
from app.modules.ui.grid import (
    UIGrid,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.widget_factory import (
    UIWidgetFactory,
)


class UIWidgetCreationService:

    def __init__(self):
        self.grid = UIGrid()

    def create(
        self,
        request: (
            UIWidgetCreationRequest
        ),
    ):
        screen = (
            ui_registry.get_screen(
                request.screen_id
            )
        )

        if (
            not screen
            or not screen.layout
        ):
            raise ValueError(
                "Screen not found"
            )

        widget = (
            UIWidgetFactory.create(
                widget_type=(
                    request.widget_type
                ),
                name=request.name,
                properties=(
                    request.properties
                ),
            )
        )

        widget.x, widget.y = (
            self.grid.snap_point(
                request.x,
                request.y,
            )
        )

        widget.style.update(
            request.style
        )

        screen.layout.add_widget(
            widget
        )

        return widget


ui_widget_creation_service = (
    UIWidgetCreationService()
)
