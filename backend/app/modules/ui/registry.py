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

    def remove_screen(
        self,
        screen_id: str,
    ):
        return self._screens.pop(
            screen_id,
            None,
        )

    def list_screens(self):
        return list(
            self._screens.values()
        )

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

    def clear(self):
        self._screens.clear()
        self._themes.clear()


ui_registry = UIRegistry()
