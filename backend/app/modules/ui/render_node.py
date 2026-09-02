from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIRenderNode:
    id: str
    node_type: str

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    style: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    children: list[
        "UIRenderNode"
    ] = field(
        default_factory=list
    )

    def add_child(
        self,
        node: "UIRenderNode",
    ):
        self.children.append(node)
        return node

    def to_dict(self):
        return {
            "id": self.id,
            "node_type": self.node_type,
            "properties": dict(
                self.properties
            ),
            "style": dict(
                self.style
            ),
            "children": [
                child.to_dict()
                for child
                in self.children
            ],
        }
