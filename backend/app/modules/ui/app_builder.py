from __future__ import annotations

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
        if self.get_screen(
            screen.id
        ):
            raise ValueError(
                "Screen already exists: "
                f"{screen.id}"
            )

        if self.get_screen_by_route(
            screen.route
        ):
            raise ValueError(
                "Screen route already exists: "
                f"{screen.route}"
            )

        self.screens.append(
            screen
        )

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

    def get_screen_by_route(
        self,
        route: str,
    ):
        for screen in self.screens:
            if screen.route == route:
                return screen

        return None

    def remove_screen(
        self,
        screen_id: str,
    ) -> bool:
        screen = self.get_screen(
            screen_id
        )

        if screen is None:
            return False

        self.screens.remove(
            screen
        )

        self.pages = [
            page
            for page
            in self.pages
            if page.screen_id
            != screen_id
        ]

        if (
            self.manifest.start_screen_id
            == screen_id
        ):
            self.manifest.start_screen_id = (
                self.screens[0].id
                if self.screens
                else None
            )

        return True

    def set_start_screen(
        self,
        screen_id: str,
    ):
        if self.get_screen(
            screen_id
        ) is None:
            raise KeyError(
                "Screen not found: "
                f"{screen_id}"
            )

        self.manifest.start_screen_id = (
            screen_id
        )

        return screen_id

    def add_page(
        self,
        page: UIPage,
    ):
        if self.get_page(
            page.id
        ):
            raise ValueError(
                "Page already exists: "
                f"{page.id}"
            )

        if self.get_screen(
            page.screen_id
        ) is None:
            raise ValueError(
                "Page references unknown screen: "
                f"{page.screen_id}"
            )

        self.pages.append(
            page
        )

        return page

    def get_page(
        self,
        page_id: str,
    ):
        for page in self.pages:
            if page.id == page_id:
                return page

        return None

    def remove_page(
        self,
        page_id: str,
    ) -> bool:
        page = self.get_page(
            page_id
        )

        if page is None:
            return False

        self.pages.remove(
            page
        )

        return True

    def set_theme(
        self,
        theme: UITheme,
    ):
        self.theme = theme

        self.manifest.theme_id = (
            theme.id
        )

        return theme

    def start_screen(self):
        if (
            self.manifest.start_screen_id
            is None
        ):
            return None

        return self.get_screen(
            self.manifest.start_screen_id
        )

    def validate(self) -> list[str]:
        errors: list[str] = []

        if not self.screens:
            errors.append(
                "Application has no screens"
            )

        if (
            self.manifest.start_screen_id
            and self.get_screen(
                self.manifest.start_screen_id
            )
            is None
        ):
            errors.append(
                "Start screen does not exist"
            )

        known_screen_ids = {
            screen.id
            for screen
            in self.screens
        }

        for page in self.pages:
            if (
                page.screen_id
                not in known_screen_ids
            ):
                errors.append(
                    "Page "
                    f"'{page.id}' references "
                    "an unknown screen"
                )

        return errors

    def to_dict(self):
        return {
            "manifest": (
                self.manifest.to_dict()
            ),
            "screens": [
                screen.to_dict()
                for screen
                in self.screens
            ],
            "pages": [
                page.to_dict()
                for page
                in self.pages
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
