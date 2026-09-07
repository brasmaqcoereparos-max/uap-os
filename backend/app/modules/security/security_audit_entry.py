from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class SecurityAuditEntry:
    action: str

    success: bool

    source: str = "security"

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
            "success": self.success,
            "source": self.source,
            "target": self.target,
            "details": dict(
                self.details
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
