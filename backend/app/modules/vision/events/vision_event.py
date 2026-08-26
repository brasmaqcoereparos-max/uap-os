from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class VisionEvent:

    event_type: str
    camera_id: str | None = None
    data: dict[str, Any] = field(
        default_factory=dict
    )
    timestamp: str = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        ).isoformat()
    )

    def to_dict(self):

        return {
            "event_type": self.event_type,
            "camera_id": self.camera_id,
            "data": dict(self.data),
            "timestamp": self.timestamp,
  }
