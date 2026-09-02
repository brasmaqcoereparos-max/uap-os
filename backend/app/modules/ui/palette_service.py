from app.modules.ui.drop_handler import (
    ui_drop_handler,
)
from app.modules.ui.drop_payload import (
    UIDropPayload,
)
from app.modules.ui.palette_defaults import (
    install_default_palette,
)
from app.modules.ui.palette_registry import (
    ui_palette_registry,
)


class UIPaletteService:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            install_default_palette()

            self._initialized = True

        return self

    def categories(self):
        self.initialize()

        return [
            category.to_dict()
            for category
            in (
                ui_palette_registry
                .categories()
            )
        ]

    def items(
        self,
        category: str | None = None,
    ):
        self.initialize()

        return [
            item.to_dict()
            for item
            in ui_palette_registry.items(
                category
            )
        ]

    def search(
        self,
        query: str,
    ):
        self.initialize()

        return [
            item.to_dict()
            for item
            in ui_palette_registry.search(
                query
            )
        ]

    def drop(
        self,
        payload: UIDropPayload,
    ):
        self.initialize()

        return (
            ui_drop_handler.handle(
                payload
            )
        )


ui_palette_service = (
    UIPaletteService()
)
