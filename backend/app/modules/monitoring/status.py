from app.modules.monitoring.diagnostic_service import (
    monitoring_diagnostic_service,
)
from app.modules.monitoring.system_health_service import (
    monitoring_system_health_service,
)


class MonitoringStatus:

    def snapshot(self):
        system = (
            monitoring_system_health_service
            .snapshot()
        )

        diagnostic = (
            monitoring_diagnostic_service
            .run()
        )

        return {
            "service": "monitoring",
            "healthy": system.healthy,
            "system": (
                system.to_dict()
            ),
            "diagnostic": (
                diagnostic.to_dict()
            ),
        }


monitoring_status = (
    MonitoringStatus()
