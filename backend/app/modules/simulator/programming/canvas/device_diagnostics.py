from app.modules.simulator.programming.canvas.device_health import (
    device_health,
)
from app.modules.simulator.programming.canvas.device_watchdog import (
    device_watchdog,
)
from app.modules.simulator.programming.canvas.device_metrics import (
    device_metrics,
)


class DeviceDiagnostics:

    def report(self):

        return {

            "health": device_health.all(),

            "watchdog": device_watchdog.all(),

            "metrics": device_metrics.all(),

        }


device_diagnostics = DeviceDiagnostics()
