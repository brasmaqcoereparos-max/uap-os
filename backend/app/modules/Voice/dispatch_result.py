from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceDispatchResult:
    accepted: bool

    status: str

    command: (
        dict[str, Any] | None
    ) = None

    confirmation_id: (
        str | None
    ) = None

    errors: list[str] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "accepted": self.accepted,
            "status": self.status,
            "command": self.command,
            "confirmation_id": (
                self.confirmation_id
            ),
            "errors": list(
                self.errors
            ),
        }
