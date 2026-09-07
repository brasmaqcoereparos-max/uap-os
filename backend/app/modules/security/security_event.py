from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class SecurityEvent:
    event_type: str

    source: str

    severity: str = "info"

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
            "event_type": (
                self.event_type
            ),
            "source": self.source,
            "severity": (
                self.severity
            ),
            "details": dict(
                self.details
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
