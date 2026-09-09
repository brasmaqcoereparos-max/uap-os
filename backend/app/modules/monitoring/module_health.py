from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.monitoring.health_state import (
    MonitoringHealthState,
)


@dataclass
class MonitoringModuleHealth:
    module: str

    state: MonitoringHealthState

    available: bool = True

    details: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "module": self.module,
            "state": self.state.value,
            "available": self.available,
            "details": dict(
                self.details
            ),
        }
