from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class CommunicationAuditEntry:
    action: str

    source: str

    success: bool

    target: str | None = None

    details: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def to_dict(self):
        return {
            "action": self.action,
            "source": self.source,
            "target": self.target,
            "success": self.success,
            "details": dict(
                self.details
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
