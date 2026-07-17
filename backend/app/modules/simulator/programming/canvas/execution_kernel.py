from app.modules.simulator.programming.canvas.execution_state_machine import (
    execution_state_machine,
)
from app.modules.simulator.programming.canvas.execution_signal import (
    execution_signal,
)
from app.modules.simulator.programming.canvas.execution_memory import (
    execution_memory,
)
from app.modules.simulator.programming.canvas.execution_io import (
    execution_io,
)


class ExecutionKernel:

    def boot(self):

        execution_state_machine.start()

        execution_memory.reset()

        execution_io.clear()

        execution_signal.clear()

    def shutdown(self):

        execution_state_machine.finish()

    def reset(self):

        execution_state_machine.stop()

        execution_memory.reset()

        execution_io.clear()

        execution_signal.clear()

    def status(self):

        return {

            "state": execution_state_machine.current(),

            "memory": execution_memory.dump(),

            "signals": execution_signal.all(),

            "io": execution_io.status(),

        }


execution_kernel = ExecutionKernel()
