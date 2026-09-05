from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class CommunicationInboundMessage:
    source: str
    channel: str
    payload: Any

    received_at: datetime = field(
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
            "source": self.source,
            "channel": self.channel,
            "payload": self.payload,
            "received_at": (
                self.received_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
  }
