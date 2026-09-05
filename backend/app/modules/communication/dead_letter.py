from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class CommunicationDeadLetter:
    message: dict[
        str,
        Any,
    ]

    reason: str

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def to_dict(self):
        return {
            "message": dict(
                self.message
            ),
            "reason": self.reason,
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
