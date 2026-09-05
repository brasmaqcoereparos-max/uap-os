from dataclasses import dataclass
from datetime import datetime
from datetime import timezone


@dataclass
class CommunicationAck:
    message_id: str

    acknowledged: bool = True

    reason: str | None = None

    created_at: datetime = (
        datetime.now(
            timezone.utc
        )
    )

    def to_dict(self):
        return {
            "message_id": (
                self.message_id
            ),
            "acknowledged": (
                self.acknowledged
            ),
            "reason": self.reason,
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
