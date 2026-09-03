from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ai.enums import (
    AIMessageRole,
)


@dataclass
class AIMessage:
    role: AIMessageRole
    content: str

    name: str | None = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "role": self.role.value,
            "content": self.content,
            "name": self.name,
            "metadata": dict(
                self.metadata
            ),
        }
