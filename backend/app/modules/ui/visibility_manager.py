from app.modules.ui.registry import (
    ui_registry,
)


class UIVisibilityManager:

    @staticmethod
    def set_widget(
        screen_id: str,
        widget_id: str,
        visible: bool,
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
            return False

        widget = (
            screen.layout.get_widget(
                widget_id
            )
        )

        if not widget:
            return False

        widget.visible = bool(
            visible
        )

        return True

    @classmethod
    def show(
        cls,
        screen_id: str,
        widget_id: str,
    ):
        return cls.set_widget(
            screen_id,
            widget_id,
            True,
        )

    @classmethod
    def hide(
        cls,
        screen_id: str,
        widget_id: str,
    ):
        return cls.set_widget(
            screen_id,
            widget_id,
            False,
        )


ui_visibility_manager = (
    UIVisibilityManager()
)
