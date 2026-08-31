from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass
class UINotification:
    id: str

    title: str
    message: str

    level: str = "info"

    duration_ms: int = 4000

    dismissible: bool = True

    data: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "level": self.level,
            "duration_ms": (
                self.duration_ms
            ),
            "dismissible": (
                self.dismissible
            ),
            "data": dict(self.data),
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
