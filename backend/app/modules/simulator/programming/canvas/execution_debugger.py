from app.modules.simulator.programming.canvas.node_breakpoints import (
    node_breakpoints,
)
from app.modules.simulator.programming.canvas.execution_stack import (
    execution_stack,
)


class ExecutionDebugger:

    def should_pause(
        self,
        node_id,
    ):

        return node_breakpoints.has(node_id)

    def enter(
        self,
        node_id,
    ):

        execution_stack.push(node_id)

    def leave(self):

        execution_stack.pop()

    def current(self):

        return execution_stack.peek()

    def stack(self):

        return execution_stack.all()


execution_debugger = ExecutionDebugger()

