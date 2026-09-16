from __future__ import annotations

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

        self.history: list[
            str
        ] = []

        self.forward_history: list[
            str
        ] = []

    def navigate(
        self,
        screen_id: str,
        *,
        add_history: bool = True,
    ):
        screen = self.registry.get_screen(
            screen_id
        )

        if not screen:
            raise ValueError(
                "Screen not found: "
                f"{screen_id}"
            )

        if (
            add_history
            and self.current_screen_id
            and self.current_screen_id
            != screen_id
        ):
            self.history.append(
                self.current_screen_id
            )

            self.forward_history.clear()

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

        if self.current_screen_id:
            self.forward_history.append(
                self.current_screen_id
            )

        self.current_screen_id = (
            screen_id
        )

        return screen

    def forward(self):
        if not self.forward_history:
            return None

        screen_id = (
            self.forward_history.pop()
        )

        screen = self.registry.get_screen(
            screen_id
        )

        if not screen:
            return None

        if self.current_screen_id:
            self.history.append(
                self.current_screen_id
            )

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

    def can_go_back(self) -> bool:
        return bool(
            self.history
        )

    def can_go_forward(self) -> bool:
        return bool(
            self.forward_history
        )

    def reset(self):
        self.current_screen_id = None
        self.history.clear()
        self.forward_history.clear()

    def snapshot(self) -> dict:
        return {
            "current_screen_id": (
                self.current_screen_id
            ),
            "history": list(
                self.history
            ),
            "forward_history": list(
                self.forward_history
            ),
        }


ui_navigation = UINavigation()
