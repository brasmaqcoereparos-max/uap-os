from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class MonitoringSystemSnapshot:
    healthy: bool

    modules: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def to_dict(self):
        return {
            "healthy": self.healthy,
            "modules": [
                dict(item)
                for item in self.modules
            ],
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
