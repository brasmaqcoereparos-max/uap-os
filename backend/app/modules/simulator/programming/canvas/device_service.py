from app.modules.simulator.programming.canvas.device_kernel import (
    device_kernel,
)
from app.modules.simulator.programming.canvas.device_statistics import (
    device_statistics,
)
from app.modules.simulator.programming.canvas.device_profiler import (
    device_profiler,
)
from app.modules.simulator.programming.canvas.device_state import (
    device_state,
    DeviceState,
)


class DeviceService:

    def initialize(self):

        device_kernel.boot()

        device_statistics.reset()

    def execute(self):

        device_kernel.execute()

    def shutdown(self):

        device_kernel.shutdown()

    def start_device(self, name):

        device_state.set(
            name,
            DeviceState.ONLINE,
        )

        device_profiler.begin(name)

    def finish_device(self, name):

        device_profiler.finish(name)

        device_statistics.executed()

    def error(self, name):

        device_state.set(
            name,
            DeviceState.ERROR,
        )

        device_statistics.error()

    def status(self):

        return {
            "kernel": device_kernel.status(),
            "statistics": device_statistics.to_dict(),
            "states": device_state.all(),
        }


device_service = DeviceService()
