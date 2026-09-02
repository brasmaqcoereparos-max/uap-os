from app.modules.ui.hierarchy_node import (
    UIHierarchyNode,
)


class UIHierarchyTree:

    def __init__(
        self,
        screen_id: str,
    ):
        self.screen_id = screen_id

        self._nodes: dict[
            str,
            UIHierarchyNode,
        ] = {}

        self._roots: list[str] = []

    def add(
        self,
        node: UIHierarchyNode,
        parent_id: str | None = None,
    ):
        if node.id in self._nodes:
            self.remove(node.id)

        node.parent_id = parent_id

        self._nodes[
            node.id
        ] = node

        if parent_id:
            parent = self.get(
                parent_id
            )

            if not parent:
                self._nodes.pop(
                    node.id,
                    None,
                )

                raise ValueError(
                    "Parent node not found"
                )

            parent.add_child(
                node.id
            )

        elif node.id not in self._roots:
            self._roots.append(
                node.id
            )

        return node

    def get(
        self,
        node_id: str,
    ):
        return self._nodes.get(
            node_id
        )

    def roots(self):
        return [
            self._nodes[node_id]
            for node_id in self._roots
            if node_id in self._nodes
        ]

    def children(
        self,
        node_id: str,
    ):
        node = self.get(
            node_id
        )

        if not node:
            return []

        return [
            self._nodes[child_id]
            for child_id
            in node.children
            if child_id in self._nodes
        ]

    def remove(
        self,
        node_id: str,
    ):
        node = self.get(
            node_id
        )

        if not node:
            return False

        for child_id in list(
            node.children
        ):
            self.remove(
                child_id
            )

        if node.parent_id:
            parent = self.get(
                node.parent_id
            )

            if parent:
                parent.remove_child(
                    node_id
                )

        elif node_id in self._roots:
            self._roots.remove(
                node_id
            )

        self._nodes.pop(
            node_id,
            None,
        )

        return True

    def clear(self):
        self._nodes.clear()
        self._roots.clear()

    def to_dict(self):
        return {
            "screen_id": self.screen_id,
            "roots": list(
                self._roots
            ),
            "nodes": {
                node_id: node.to_dict()
                for node_id, node
                in self._nodes.items()
            },
      }
