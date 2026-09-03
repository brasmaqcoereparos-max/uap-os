from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIProjectRequirement:
    id: str
    name: str

    requirement_type: str = "general"

    description: str = ""

    required: bool = True

    value: Any = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "requirement_type": (
                self.requirement_type
            ),
            "description": (
                self.description
            ),
            "required": self.required,
            "value": self.value,
            "metadata": dict(
                self.metadata
            ),
        }
