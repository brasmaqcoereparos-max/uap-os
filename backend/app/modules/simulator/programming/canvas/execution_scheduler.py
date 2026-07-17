from app.modules.simulator.programming.canvas.execution_queue import (
    execution_queue,
)
from app.modules.simulator.programming.canvas.node_runtime import (
    node_runtime,
)


class ExecutionScheduler:

    def execute(self):

        while not execution_queue.empty():

            node = execution_queue.next()

            node_runtime.start(node)

            node_runtime.finish(node)

    def enqueue(
        self,
        node_id,
    ):

        execution_queue.add(node_id)

    def clear(self):

        execution_queue.clear()


execution_scheduler = ExecutionScheduler()
