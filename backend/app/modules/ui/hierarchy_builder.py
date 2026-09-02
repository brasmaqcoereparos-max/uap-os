from app.modules.ui.hierarchy_node import (
    UIHierarchyNode,
)
from app.modules.ui.hierarchy_tree import (
    UIHierarchyTree,
)


class UIHierarchyBuilder:

    @staticmethod
    def from_screen(
        screen,
    ):
        tree = UIHierarchyTree(
            screen_id=screen.id
        )

        root = UIHierarchyNode(
            id=f"screen:{screen.id}",
            name=screen.name,
            node_type="screen",
        )

        tree.add(root)

        if not screen.layout:
            return tree

        layout_node = UIHierarchyNode(
            id=f"layout:{screen.layout.id}",
            name=screen.layout.name,
            node_type="layout",
        )

        tree.add(
            layout_node,
            parent_id=root.id,
        )

        for widget in (
            screen.layout.widgets
        ):
            widget_node = (
                UIHierarchyNode(
                    id=widget.id,
                    name=widget.name,
                    node_type="widget",
                    visible=widget.visible,
                    metadata={
                        "widget_type": (
                            widget
                            .widget_type
                            .value
                        )
                    },
                )
            )

            tree.add(
                widget_node,
                parent_id=(
                    layout_node.id
                ),
            )

        return tree


ui_hierarchy_builder = (
    UIHierarchyBuilder()
      )
