import uuid
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone

from app.modules.voice.command import (
    VoiceCommand,
)


@dataclass
class VoiceConfirmation:
    command: VoiceCommand

    id: str = field(
        default_factory=lambda: (
            str(uuid.uuid4())
        )
    )

    confirmed: bool = False
    cancelled: bool = False

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def confirm(self):
        if self.cancelled:
            return False

        self.confirmed = True

        return True

    def cancel(self):
        if self.confirmed:
            return False

        self.cancelled = True

        return True

    def pending(self):
        return (
            not self.confirmed
            and not self.cancelled
        )

    def to_dict(self):
        return {
            "id": self.id,
            "command": (
                self.command.to_dict()
            ),
            "confirmed": self.confirmed,
            "cancelled": self.cancelled,
            "pending": self.pending(),
            "created_at": (
                self.created_at
                .isoformat()
            ),
          }
