from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIAnimation:
    id: str
    name: str

    property_name: str

    from_value: Any = None
    to_value: Any = None

    duration_ms: int = 300
    delay_ms: int = 0

    easing: str = "linear"

    iterations: int = 1

    alternate: bool = False

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "property_name": (
                self.property_name
            ),
            "from_value": self.from_value,
            "to_value": self.to_value,
            "duration_ms": self.duration_ms,
            "delay_ms": self.delay_ms,
            "easing": self.easing,
            "iterations": self.iterations,
            "alternate": self.alternate,
            "metadata": dict(
                self.metadata
            ),
        }
