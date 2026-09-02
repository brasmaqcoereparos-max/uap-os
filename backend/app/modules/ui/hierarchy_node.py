from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIHierarchyNode:
    id: str
    name: str
    node_type: str

    parent_id: str | None = None

    children: list[str] = field(
        default_factory=list
    )

    visible: bool = True
    locked: bool = False
    expanded: bool = True

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_child(
        self,
        child_id: str,
    ):
        if child_id not in self.children:
            self.children.append(
                child_id
            )

        return child_id

    def remove_child(
        self,
        child_id: str,
    ):
        if child_id not in self.children:
            return False

        self.children.remove(
            child_id
        )

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "node_type": self.node_type,
            "parent_id": self.parent_id,
            "children": list(
                self.children
            ),
            "visible": self.visible,
            "locked": self.locked,
            "expanded": self.expanded,
            "metadata": dict(
                self.metadata
            ),
      }
