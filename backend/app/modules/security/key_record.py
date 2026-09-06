from dataclasses import dataclass
from datetime import datetime
from datetime import timezone


@dataclass
class SecurityKeyRecord:
    key_id: str

    active: bool = True

    created_at: datetime = (
        datetime.now(
            timezone.utc
        )
    )

    rotated_from: str | None = None

    def to_dict(self):
        return {
            "key_id": self.key_id,
            "active": self.active,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "rotated_from": (
                self.rotated_from
            ),
        }
