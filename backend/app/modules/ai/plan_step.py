from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIPlanStep:
    id: str
    title: str

    description: str = ""

    order: int = 0

    status: str = "pending"

    depends_on: list[str] = field(
        default_factory=list
    )

    inputs: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    outputs: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": (
                self.description
            ),
            "order": self.order,
            "status": self.status,
            "depends_on": list(
                self.depends_on
            ),
            "inputs": dict(
                self.inputs
            ),
            "outputs": dict(
                self.outputs
            ),
            "metadata": dict(
                self.metadata
            ),
        }
