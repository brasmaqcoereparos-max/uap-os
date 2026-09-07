from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class SecuritySession:
    session_id: str

    principal_id: str

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    last_activity_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def touch(self):
        self.last_activity_at = (
            datetime.now(
                timezone.utc
            )
        )

        return self.last_activity_at

    def close(self):
        self.active = False

        return True

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "principal_id": (
                self.principal_id
            ),
            "active": self.active,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "last_activity_at": (
                self.last_activity_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
  }
