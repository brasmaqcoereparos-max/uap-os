from app.modules.ui.hierarchy_builder import (
    ui_hierarchy_builder,
)
from app.modules.ui.hierarchy_registry import (
    ui_hierarchy_registry,
)
from app.modules.ui.registry import (
    ui_registry,
)


class UIHierarchyService:

    def rebuild(
        self,
        screen_id: str,
    ):
        screen = (
            ui_registry.get_screen(
                screen_id
            )
        )

        if not screen:
            raise ValueError(
                "Screen not found"
            )

        tree = (
            ui_hierarchy_builder
            .from_screen(
                screen
            )
        )

        return (
            ui_hierarchy_registry
            .register(tree)
        )

    def get(
        self,
        screen_id: str,
        rebuild: bool = False,
    ):
        if not rebuild:
            tree = (
                ui_hierarchy_registry
                .get(screen_id)
            )

            if tree:
                return tree

        return self.rebuild(
            screen_id
        )

    def snapshot(
        self,
        screen_id: str,
    ):
        return self.get(
            screen_id
        ).to_dict()


ui_hierarchy_service = (
    UIHierarchyService()
)
