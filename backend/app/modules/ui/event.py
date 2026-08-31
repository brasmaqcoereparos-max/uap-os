from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass
class UIEvent:
    name: str

    widget_id: str | None = None
    screen_id: str | None = None

    payload: dict[str, Any] = field(
        default_factory=dict
    )

    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )

    def to_dict(self):
        return {
            "name": self.name,
            "widget_id": self.widget_id,
            "screen_id": self.screen_id,
            "payload": dict(self.payload),
            "timestamp": (
                self.timestamp.isoformat()
            ),
        }
