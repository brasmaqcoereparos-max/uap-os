from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any

from app.modules.communication.connection_state import (
    CommunicationConnectionState,
)


@dataclass
class CommunicationConnection:
    id: str

    transport: str
    destination: str

    state: CommunicationConnectionState = (
        CommunicationConnectionState.DISCONNECTED
    )

    connected_at: datetime | None = None
    last_activity_at: datetime | None = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def connect(self):
        self.state = (
            CommunicationConnectionState.CONNECTED
        )

        now = datetime.now(
            timezone.utc
        )

        self.connected_at = now
        self.last_activity_at = now

        return self

    def disconnect(self):
        self.state = (
            CommunicationConnectionState.DISCONNECTED
        )

        return self

    def touch(self):
        self.last_activity_at = (
            datetime.now(
                timezone.utc
            )
        )

        return self.last_activity_at

    def to_dict(self):
        return {
            "id": self.id,
            "transport": self.transport,
            "destination": (
                self.destination
            ),
            "state": self.state.value,
            "connected_at": (
                self.connected_at.isoformat()
                if self.connected_at
                else None
            ),
            "last_activity_at": (
                self.last_activity_at
                .isoformat()
                if self.last_activity_at
                else None
            ),
            "metadata": dict(
                self.metadata
            ),
  }
