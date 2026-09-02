from dataclasses import dataclass
from dataclasses import field

from app.modules.ui.app_manifest import (
    UIAppManifest,
)
from app.modules.ui.page import (
    UIPage,
)
from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.theme import (
    UITheme,
)


@dataclass
class UIApp:
    manifest: UIAppManifest

    screens: list[
        UIScreen
    ] = field(
        default_factory=list
    )

    pages: list[
        UIPage
    ] = field(
        default_factory=list
    )

    theme: UITheme | None = None

    def add_screen(
        self,
        screen: UIScreen,
    ):
        if self.get_screen(screen.id):
            raise ValueError(
                "Screen already exists: "
                f"{screen.id}"
            )

        self.screens.append(screen)

        if (
            self.manifest.start_screen_id
            is None
        ):
            self.manifest.start_screen_id = (
                screen.id
            )

        return screen

    def get_screen(
        self,
        screen_id: str,
    ):
        for screen in self.screens:
            if screen.id == screen_id:
                return screen

        return None

    def add_page(
        self,
        page: UIPage,
    ):
        self.pages.append(page)

        return page

    def set_theme(
        self,
        theme: UITheme,
    ):
        self.theme = theme

        self.manifest.theme_id = theme.id

        return theme

    def to_dict(self):
        return {
            "manifest": (
                self.manifest.to_dict()
            ),
            "screens": [
                screen.to_dict()
                for screen in self.screens
            ],
            "pages": [
                page.to_dict()
                for page in self.pages
            ],
            "theme": (
                self.theme.to_dict()
                if self.theme
                else None
            ),
        }


class UIAppBuilder:

    @staticmethod
    def create(
        app_id: str,
        name: str,
        version: str = "1.0.0",
    ):
        manifest = UIAppManifest(
            id=app_id,
            name=name,
            version=version,
        )

        return UIApp(
            manifest=manifest
        )
