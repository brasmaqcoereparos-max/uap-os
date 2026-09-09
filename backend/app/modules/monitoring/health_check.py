from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.monitoring.health_state import (
    MonitoringHealthState,
)


@dataclass
class MonitoringHealthCheck:
    name: str

    state: MonitoringHealthState

    message: str = ""

    details: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "state": self.state.value,
            "message": self.message,
            "details": dict(
                self.details
            ),
        }
