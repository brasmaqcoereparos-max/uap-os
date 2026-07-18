from app.modules.simulator.programming.canvas.execution_kernel import (
    execution_kernel,
)
from app.modules.simulator.programming.canvas.execution_clock import (
    execution_clock,
)
from app.modules.simulator.programming.canvas.execution_ports import (
    execution_ports,
)
from app.modules.simulator.programming.canvas.execution_devices import (
    execution_devices,
)


class ExecutionRuntime:

    def initialize(self):

        execution_kernel.boot()

        execution_clock.start()

        execution_ports.reset()

        execution_devices.clear()

    def shutdown(self):

        execution_kernel.shutdown()

    def status(self):

        return {

            "kernel": execution_kernel.status(),

            "clock_ms": execution_clock.millis(),

            "clock_sec": execution_clock.seconds(),

            "ports": execution_ports.status(),

            "devices": list(

                execution_devices.all().keys()

            ),

        }


execution_runtime = ExecutionRuntime()
