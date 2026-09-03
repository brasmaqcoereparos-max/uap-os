from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AITask:
    id: str
    title: str

    description: str = ""

    task_type: str = "general"

    priority: int = 0

    parameters: dict[
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
            "task_type": (
                self.task_type
            ),
            "priority": (
                self.priority
            ),
            "parameters": dict(
                self.parameters
            ),
            "metadata": dict(
                self.metadata
            ),
        }
