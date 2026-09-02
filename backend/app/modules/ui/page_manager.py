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

    def get(
        self,
        page_id: str,
    ):
        return self._pages.get(
            page_id
        )

    def remove(
        self,
        page_id: str,
    ):
        return self._pages.pop(
            page_id,
            None,
        )

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
            for page in self.list_all()
            if page.enabled
        ]

    def clear(self):
        self._pages.clear()


ui_page_manager = UIPageManager()
