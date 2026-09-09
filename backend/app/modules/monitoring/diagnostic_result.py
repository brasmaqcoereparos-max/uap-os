from dataclasses import dataclass
from dataclasses import field

from app.modules.monitoring.health_check import (
    MonitoringHealthCheck,
)


@dataclass
class MonitoringDiagnosticResult:
    healthy: bool

    checks: list[
        MonitoringHealthCheck
    ] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "healthy": self.healthy,
            "checks": [
                check.to_dict()
                for check in self.checks
            ],
        }
