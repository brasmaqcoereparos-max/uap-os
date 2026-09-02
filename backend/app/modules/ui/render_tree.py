from dataclasses import dataclass
from dataclasses import field

from app.modules.ui.render_node import (
    UIRenderNode,
)


@dataclass
class UIRenderTree:
    screen_id: str

    width: float
    height: float

    root: UIRenderNode

    metadata: dict = field(
        default_factory=dict
    )

    def find(
        self,
        node_id: str,
    ):
        def walk(
            node: UIRenderNode,
        ):
            if node.id == node_id:
                return node

            for child in node.children:
                result = walk(child)

                if result:
                    return result

            return None

        return walk(self.root)

    def to_dict(self):
        return {
            "screen_id": (
                self.screen_id
            ),
            "width": self.width,
            "height": self.height,
            "root": (
                self.root.to_dict()
            ),
            "metadata": dict(
                self.metadata
            ),
              }
