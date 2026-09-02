from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIDropPayload:
    palette_item_id: str

    x: float
    y: float

    screen_id: str

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    source: str = "palette"

    def to_dict(self):
        return {
            "palette_item_id": (
                self.palette_item_id
            ),
            "x": self.x,
            "y": self.y,
            "screen_id": (
                self.screen_id
            ),
            "properties": dict(
                self.properties
            ),
            "source": self.source,
        }
