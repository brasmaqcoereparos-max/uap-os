from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIToolDefinition:
    name: str

    description: str = ""

    target: str = "application"

    parameters_schema: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    requires_review: bool = True

    enabled: bool = True

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "description": (
                self.description
            ),
            "target": self.target,
            "parameters_schema": dict(
                self.parameters_schema
            ),
            "requires_review": (
                self.requires_review
            ),
            "enabled": self.enabled,
            "metadata": dict(
                self.metadata
            ),
        }
