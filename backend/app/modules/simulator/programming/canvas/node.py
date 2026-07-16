from dataclasses import dataclass, field
import uuid


@dataclass
class Node:

    name: str

    block_type: str

    x: int = 100

    y: int = 100

    width: int = 180

    height: int = 60

    selected: bool = False

    locked: bool = False

    visible: bool = True

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    config: dict = field(
        default_factory=dict
    )

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "type": self.block_type,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "selected": self.selected,
            "locked": self.locked,
            "visible": self.visible,
            "config": self.config,
        }
