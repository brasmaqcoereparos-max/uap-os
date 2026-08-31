from app.modules.ui.registry import (
    UIRegistry,
    ui_registry,
)


class UINavigation:

    def __init__(
        self,
        registry: UIRegistry = ui_registry,
    ):
        self.registry = registry

        self.current_screen_id: (
            str | None
        ) = None

        self.history: list[str] = []

    def navigate(
        self,
        screen_id: str,
    ):
        screen = self.registry.get_screen(
            screen_id
        )

        if not screen:
            raise ValueError(
                f"Screen not found: "
                f"{screen_id}"
            )

        if self.current_screen_id:
            self.history.append(
                self.current_screen_id
            )

        self.current_screen_id = (
            screen_id
        )

        return screen

    def back(self):
        if not self.history:
            return None

        screen_id = self.history.pop()

        screen = self.registry.get_screen(
            screen_id
        )

        if not screen:
            return None

        self.current_screen_id = (
            screen_id
        )

        return screen

    def current(self):
        if not self.current_screen_id:
            return None

        return self.registry.get_screen(
            self.current_screen_id
        )

    def reset(self):
        self.current_screen_id = None
        self.history.clear()


ui_navigation = UINavigation()
