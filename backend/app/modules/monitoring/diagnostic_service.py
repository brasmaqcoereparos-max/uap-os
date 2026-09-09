from app.modules.monitoring.diagnostic_result import (
    MonitoringDiagnosticResult,
)
from app.modules.monitoring.health_check import (
    MonitoringHealthCheck,
)
from app.modules.monitoring.health_state import (
    MonitoringHealthState,
)
from app.modules.monitoring.module_health_registry import (
    monitoring_module_health_registry,
)


class MonitoringDiagnosticService:

    def run(self):
        checks = []

        for module in (
            monitoring_module_health_registry
            .list_all()
        ):
            checks.append(
                MonitoringHealthCheck(
                    name=module.module,
                    state=module.state,
                    message=(
                        "Module healthy"
                        if (
                            module.state
                            == MonitoringHealthState.HEALTHY
                        )
                        else (
                            "Module requires "
                            "attention"
                        )
                    ),
                    details=dict(
                        module.details
                    ),
                )
            )

        healthy = all(
            check.state
            == MonitoringHealthState.HEALTHY
            for check in checks
        )

        return (
            MonitoringDiagnosticResult(
                healthy=healthy,
                checks=checks,
            )
        )


monitoring_diagnostic_service = (
    MonitoringDiagnosticService()
)
