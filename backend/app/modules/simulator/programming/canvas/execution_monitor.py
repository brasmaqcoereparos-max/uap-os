from app.modules.simulator.programming.canvas.execution_statistics import (
    execution_statistics,
)
from app.modules.simulator.programming.canvas.execution_profiler import (
    execution_profiler,
)


class ExecutionMonitor:

    def begin(self):

        execution_statistics.reset()

        execution_profiler.start()

    def executed(
        self,
        node_id,
        elapsed=0,
    ):

        execution_statistics.node_executed()

        execution_profiler.node(
            node_id,
            elapsed,
        )

    def error(self):

        execution_statistics.node_error()

    def finish(self):

        execution_statistics.finish()

        execution_profiler.finish()

    def report(self):

        return {

            "statistics": execution_statistics.to_dict(),

            "sessions": execution_profiler.all(),

        }


execution_monitor = ExecutionMonitor()
