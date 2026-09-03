from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceExecutionResult:
    executed: bool

    status: str

    result: Any = None

    command: (
        dict[str, Any] | None
    ) = None

    errors: list[str] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "executed": self.executed,
            "status": self.status,
            "result": self.result,
            "command": self.command,
            "errors": list(
                self.errors
            ),
        }
