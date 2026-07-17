
from app.modules.simulator.programming.canvas.execution_manager import (
    execution_manager,
)
from app.modules.simulator.programming.canvas.execution_history import (
    execution_history,
)
from app.modules.simulator.programming.canvas.execution_timer import (
    execution_timer,
)


class ExecutionController:

    def execute(self):

        execution_timer.start()

        result = execution_manager.execute()

        execution_timer.stop()

        result["elapsed"] = execution_timer.elapsed()

        execution_history.add(result)

        return result

    def last(self):

        return execution_history.last()

    def history(self):

        return execution_history.all()

    def clear_history(self):

        execution_history.clear()


execution_controller = ExecutionController()
