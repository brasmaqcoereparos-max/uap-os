import json

from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.theme import (
    UITheme,
)


class UISerializer:

    @staticmethod
    def screen_to_dict(
        screen: UIScreen,
    ):
        return screen.to_dict()

    @staticmethod
    def screen_to_json(
        screen: UIScreen,
    ):
        return json.dumps(
            screen.to_dict(),
            ensure_ascii=False,
            indent=2,
        )

    @staticmethod
    def theme_to_dict(
        theme: UITheme,
    ):
        return theme.to_dict()

    @staticmethod
    def theme_to_json(
        theme: UITheme,
    ):
        return json.dumps(
            theme.to_dict(),
            ensure_ascii=False,
            indent=2,
        )
