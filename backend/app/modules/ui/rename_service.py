from app.modules.ui.lock_manager import (
    ui_lock_manager,
)
from app.modules.ui.registry import (
    ui_registry,
)


class UIRenameService:

    def rename_widget(
        self,
        screen_id: str,
        widget_id: str,
        name: str,
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

        normalized = name.strip()

        if not normalized:
            raise ValueError(
                "Widget name cannot "
                "be empty"
            )

        widget.name = normalized

        return widget


ui_rename_service = (
    UIRenameService()
      )
