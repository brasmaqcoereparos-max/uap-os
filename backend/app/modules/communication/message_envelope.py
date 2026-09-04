from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class CommunicationMessageEnvelope:
    id: str

    topic: str

    source: str

    payload: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    target: str | None = None

    correlation_id: str | None = None

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

    def to_dict(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "source": self.source,
            "target": self.target,
            "correlation_id": (
                self.correlation_id
            ),
            "payload": dict(
                self.payload
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
  }
