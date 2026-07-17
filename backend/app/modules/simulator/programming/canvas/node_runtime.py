from app.modules.simulator.programming.canvas.node_execution_state import (
    node_execution_state,
    ExecutionState,
)
from app.modules.simulator.programming.canvas.node_logger import (
    node_logger,
)
from app.modules.simulator.programming.canvas.node_profiler import (
    node_profiler,
)


class NodeRuntime:

    def start(
        self,
        node_id,
    ):

        node_execution_state.set_state(

            node_id,

            ExecutionState.RUNNING,

        )

        node_profiler.begin(node_id)

        node_logger.log(

            "INFO",

            node_id,

            "Execution started",

        )

    def finish(
        self,
        node_id,
    ):

        node_profiler.finish(node_id)

        node_execution_state.set_state(

            node_id,

            ExecutionState.SUCCESS,

        )

        node_logger.log(

            "INFO",

            node_id,

            "Execution finished",

        )

    def error(
        self,
        node_id,
        message,
    ):

        node_execution_state.set_state(

            node_id,

            ExecutionState.ERROR,

        )

        node_logger.log(

            "ERROR",

            node_id,

            message,

        )


node_runtime = NodeRuntime()
