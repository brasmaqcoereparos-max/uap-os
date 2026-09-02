from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIPanel:
    id: str
    name: str

    title: str = ""

    position: str = "left"

    width: float = 280
    height: float | None = None

    visible: bool = True
    collapsed: bool = False
    resizable: bool = True

    order: int = 0

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def show(self):
        self.visible = True
        return self

    def hide(self):
        self.visible = False
        return self

    def collapse(self):
        self.collapsed = True
        return self

    def expand(self):
        self.collapsed = False
        return self

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": (
                self.title
                or self.name
            ),
            "position": self.position,
            "width": self.width,
            "height": self.height,
            "visible": self.visible,
            "collapsed": (
                self.collapsed
            ),
            "resizable": (
                self.resizable
            ),
            "order": self.order,
            "metadata": dict(
                self.metadata
            ),
  }
