from app.modules.monitoring.diagnostic_service import (
    monitoring_diagnostic_service,
)
from app.modules.monitoring.status import (
    monitoring_status,
)
from app.modules.monitoring.system_health_service import (
    monitoring_system_health_service,
)


class MonitoringFacade:

    def report_module(
        self,
        module: str,
        healthy: bool,
        details: dict | None = None,
    ):
        result = (
            monitoring_system_health_service
            .report(
                module=module,
                healthy=healthy,
                details=details,
            )
        )

        return result.to_dict()

    def diagnose(self):
        return (
            monitoring_diagnostic_service
            .run()
            .to_dict()
        )

    def status(self):
        return (
            monitoring_status
            .snapshot()
        )


monitoring_facade = (
    MonitoringFacade()
)
