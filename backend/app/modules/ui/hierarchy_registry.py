from app.modules.ui.hierarchy_tree import (
    UIHierarchyTree,
)


class UIHierarchyRegistry:

    def __init__(self):
        self._trees: dict[
            str,
            UIHierarchyTree,
        ] = {}

    def register(
        self,
        tree: UIHierarchyTree,
    ):
        self._trees[
            tree.screen_id
        ] = tree

        return tree

    def get(
        self,
        screen_id: str,
    ):
        return self._trees.get(
            screen_id
        )

    def remove(
        self,
        screen_id: str,
    ):
        return self._trees.pop(
            screen_id,
            None,
        )

    def list_all(self):
        return list(
            self._trees.values()
        )

    def clear(self):
        self._trees.clear()


ui_hierarchy_registry = (
    UIHierarchyRegistry()
)
