from dataclasses import dataclass, field
import uuid


@dataclass
class Node:

    name: str

    block_type: str

    x: int = 100

    y: int = 100

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    config: dict = field(default_factory=dict)

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "type": self.block_type,
            "x": self.x,
            "y": self.y,
            "config": self.config,
        }
