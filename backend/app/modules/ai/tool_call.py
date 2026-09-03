from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIToolCall:
    tool: str

    arguments: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    source: str = "ai"

    approved: bool = False

    def approve(self):
        self.approved = True

        return True

    def to_dict(self):
        return {
            "tool": self.tool,
            "arguments": dict(
                self.arguments
            ),
            "source": self.source,
            "approved": (
                self.approved
            ),
        }
