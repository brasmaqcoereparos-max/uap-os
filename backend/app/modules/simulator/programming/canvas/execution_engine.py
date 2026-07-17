from app.modules.simulator.programming.canvas.execution_scheduler import (
    execution_scheduler,
)
from app.modules.simulator.programming.canvas.execution_result import (
    ExecutionResult,
)
from app.modules.simulator.programming.canvas.execution_queue import (
    execution_queue,
)


class ExecutionEngine:

    def run(self):

        result = ExecutionResult()

        while not execution_queue.empty():

            node = execution_queue.next()

            try:

                execution_scheduler.enqueue(node)

                execution_scheduler.execute()

                result.add_node(node)

            except Exception as exc:

                result.add_error(

                    node,

                    str(exc),

                )

        result.finish()

        return result.to_dict()


execution_engine = ExecutionEngine()
