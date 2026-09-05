from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class CommunicationSession:
    id: str

    connection_id: str

    active: bool = True

    created_at: datetime = field(
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

    def close(self):
        self.active = False

        return self

    def to_dict(self):
        return {
            "id": self.id,
            "connection_id": (
                self.connection_id
            ),
            "active": self.active,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
        }
