from app.modules.simulator.programming.canvas.device_runtime import (
    device_runtime,
)
from app.modules.simulator.programming.canvas.device_scheduler import (
    device_scheduler,
)
from app.modules.simulator.programming.canvas.device_memory import (
    device_memory,
)
from app.modules.simulator.programming.canvas.device_logger import (
    device_logger,
)


class DeviceKernel:

    def boot(self):

        device_runtime.initialize()

        device_logger.log(

            "kernel",

            "INFO",

            "Kernel initialized",

        )

    def execute(self):

        device_scheduler.execute()

    def shutdown(self):

        device_runtime.shutdown()

        device_memory.clear()

        device_logger.log(

            "kernel",

            "INFO",

            "Kernel shutdown",

        )

    def status(self):

        return {

            "runtime": device_runtime.status(),

            "memory": device_memory.dump(),

            "logs": len(device_logger.all()),

        }


device_kernel = DeviceKernel()
