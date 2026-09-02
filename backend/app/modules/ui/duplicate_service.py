import copy
import uuid

from app.modules.ui.lock_manager import (
    ui_lock_manager,
)
from app.modules.ui.registry import (
    ui_registry,
)


class UIDuplicateService:

    def duplicate(
        self,
        screen_id: str,
        widget_id: str,
        offset_x: float = 20,
        offset_y: float = 20,
    ):
        screen = (
            ui_registry.get_screen(
                screen_id
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
            screen.layout.get_widget(
                widget_id
            )
        )

        if not widget:
            raise ValueError(
                "Widget not found"
            )

        if ui_lock_manager.is_locked(
            widget_id
        ):
            raise ValueError(
                "Widget is locked"
            )

        duplicate = copy.deepcopy(
            widget
        )

        duplicate.id = str(
            uuid.uuid4()
        )

        duplicate.name = (
            f"{widget.name} Copy"
        )

        duplicate.x += offset_x
        duplicate.y += offset_y

        screen.layout.add_widget(
            duplicate
        )

        return duplicate


ui_duplicate_service = (
    UIDuplicateService()
)
