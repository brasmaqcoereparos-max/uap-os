from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AISimulationTestCase:
    id: str
    name: str

    input_data: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    expected: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    enabled: bool = True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "input_data": dict(
                self.input_data
            ),
            "expected": dict(
                self.expected
            ),
            "enabled": self.enabled,
        }
