from app.modules.monitoring.module_health import (
    MonitoringModuleHealth,
)


class MonitoringModuleHealthRegistry:

    def __init__(self):
        self._modules: dict[
            str,
            MonitoringModuleHealth,
        ] = {}

    def register(
        self,
        health: MonitoringModuleHealth,
    ):
        self._modules[
            health.module
        ] = health

        return health

    def get(
        self,
        module: str,
    ):
        return self._modules.get(
            module
        )

    def list_all(self):
        return list(
            self._modules.values()
        )

    def clear(self):
        self._modules.clear()


monitoring_module_health_registry = (
    MonitoringModuleHealthRegistry()
)
