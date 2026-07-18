from app.modules.simulator.programming.canvas.device_manager import (
    device_manager,
)
from app.modules.simulator.programming.canvas.device_simulator import (
    device_simulator,
)


class DeviceRuntime:

    def initialize(self):

        device_simulator.start()

    def shutdown(self):

        device_simulator.stop()

        device_manager.clear()

    def status(self):

        return {

            "simulator": device_simulator.status(),

            "devices": device_manager.all(),

        }


device_runtime = DeviceRuntime()
