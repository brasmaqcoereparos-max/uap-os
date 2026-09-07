from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class TamperEvent:
    event_type: str

    target: str

    detected: bool = True

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
            "target": self.target,
            "detected": (
                self.detected
            ),
            "details": dict(
                self.details
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
              }
