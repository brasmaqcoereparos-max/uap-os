from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AISimulationScenario:
    name: str

    description: str = ""

    devices: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    inputs: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    expected_outputs: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    steps: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "name": self.name,
            "description": (
                self.description
            ),
            "devices": [
                dict(item)
                for item in self.devices
            ],
            "inputs": [
                dict(item)
                for item in self.inputs
            ],
            "expected_outputs": [
                dict(item)
                for item
                in self.expected_outputs
            ],
            "steps": [
                dict(item)
                for item in self.steps
            ],
  }
