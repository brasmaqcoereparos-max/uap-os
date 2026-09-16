from __future__ import annotations

from app.modules.ui.page import (
    UIPage,
)


class UIPageManager:

    def __init__(self):
        self._pages: dict[
            str,
            UIPage,
        ] = {}

    def register(
        self,
        page: UIPage,
    ):
        self._pages[
            page.id
        ] = page

        return page

    def create(
        self,
        page_id: str,
        name: str,
        screen_id: str,
        order: int = 0,
        enabled: bool = True,
        icon: str | None = None,
    ) -> UIPage:
        if page_id in self._pages:
            raise ValueError(
                "Page already exists: "
                f"{page_id}"
            )

        page = UIPage(
            id=page_id,
            name=name,
            screen_id=screen_id,
            order=order,
            enabled=enabled,
            icon=icon,
        )

        return self.register(
            page
        )

    def get(
        self,
        page_id: str,
    ):
        return self._pages.get(
            page_id
        )

    def require(
        self,
        page_id: str,
    ) -> UIPage:
        page = self.get(
            page_id
        )

        if page is None:
            raise KeyError(
                f"Page not found: {page_id}"
            )

        return page

    def get_by_screen(
        self,
        screen_id: str,
    ) -> UIPage | None:
        for page in self._pages.values():
            if page.screen_id == screen_id:
                return page

        return None

    def remove(
        self,
        page_id: str,
    ):
        return self._pages.pop(
            page_id,
            None,
        )

    def enable(
        self,
        page_id: str,
    ) -> bool:
        page = self.get(
            page_id
        )

        if page is None:
            return False

        page.enable()

        return True

    def disable(
        self,
        page_id: str,
    ) -> bool:
        page = self.get(
            page_id
        )

        if page is None:
            return False

        page.disable()

        return True

    def list_all(self):
        return sorted(
            self._pages.values(),
            key=lambda page: (
                page.order,
                page.name,
            ),
        )

    def enabled_pages(self):
        return [
            page
            for page
            in self.list_all()
            if page.enabled
        ]

    def snapshot(self) -> list[dict]:
        return [
            page.to_dict()
            for page
            in self.list_all()
        ]

    def clear(self):
        self._pages.clear()


ui_page_manager = UIPageManager()
