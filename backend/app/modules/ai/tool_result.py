from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIToolResult:
    tool: str

    success: bool

    result: Any = None

    error: str | None = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "tool": self.tool,
            "success": self.success,
            "result": self.result,
            "error": self.error,
            "metadata": dict(
                self.metadata
            ),
        }
