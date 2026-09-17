from __future__ import annotations

from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.theme import (
    UITheme,
)


class UIRegistry:

    def __init__(self):
        self._screens: dict[
            str,
            UIScreen,
        ] = {}

        self._themes: dict[
            str,
            UITheme,
        ] = {}

    def register_screen(
        self,
        screen: UIScreen,
    ):
        existing_route = (
            self.get_screen_by_route(
                screen.route
            )
        )

        if (
            existing_route is not None
            and existing_route.id
            != screen.id
        ):
            raise ValueError(
                "Screen route already registered: "
                f"{screen.route}"
            )

        self._screens[
            screen.id
        ] = screen

        return screen

    def get_screen(
        self,
        screen_id: str,
    ):
        return self._screens.get(
            screen_id
        )

    def require_screen(
        self,
        screen_id: str,
    ) -> UIScreen:
        screen = self.get_screen(
            screen_id
        )

        if screen is None:
            raise KeyError(
                "Screen not found: "
                f"{screen_id}"
            )

        return screen

    def get_screen_by_route(
        self,
        route: str,
    ) -> UIScreen | None:
        if not route:
            route = "/"

        if not route.startswith("/"):
            route = "/" + route

        for screen in (
            self._screens.values()
        ):
            if screen.route == route:
                return screen

        return None

    def remove_screen(
        self,
        screen_id: str,
    ):
        return self._screens.pop(
            screen_id,
            None,
        )

    def list_screens(
        self,
        visible_only: bool = False,
        enabled_only: bool = False,
    ):
        screens = list(
            self._screens.values()
        )

        if visible_only:
            screens = [
                screen
                for screen
                in screens
                if screen.visible
            ]

        if enabled_only:
            screens = [
                screen
                for screen
                in screens
                if screen.enabled
            ]

        return screens

    def register_theme(
        self,
        theme: UITheme,
    ):
        self._themes[
            theme.id
        ] = theme

        return theme

    def get_theme(
        self,
        theme_id: str,
    ):
        return self._themes.get(
            theme_id
        )

    def require_theme(
        self,
        theme_id: str,
    ) -> UITheme:
        theme = self.get_theme(
            theme_id
        )

        if theme is None:
            raise KeyError(
                "Theme not found: "
                f"{theme_id}"
            )

        return theme

    def remove_theme(
        self,
        theme_id: str,
    ):
        return self._themes.pop(
            theme_id,
            None,
        )

    def list_themes(self):
        return list(
            self._themes.values()
        )

    def snapshot(self):
        return {
            "screens": [
                screen.to_dict()
                for screen
                in self.list_screens()
            ],
            "themes": [
                theme.to_dict()
                for theme
                in self.list_themes()
            ],
        }

    def clear(self):
        self._screens.clear()
        self._themes.clear()


ui_registry = UIRegistry()
