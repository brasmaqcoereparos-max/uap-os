from app.modules.simulator.programming.canvas.execution_session import (
    ExecutionSession,
)
from app.modules.simulator.programming.canvas.execution_monitor import (
    execution_monitor,
)
from app.modules.simulator.programming.canvas.execution_engine import (
    execution_engine,
)


class ExecutionManager:

    def __init__(self):

        self.session = None

    def execute(self):

        self.session = ExecutionSession()

        self.session.start()

        execution_monitor.begin()

        try:

            result = execution_engine.run()

            self.session.finish()

            execution_monitor.finish()

            return {

                "session": self.session.to_dict(),

                "result": result,

                "monitor": execution_monitor.report(),

            }

        except Exception:

            self.session.error()

            execution_monitor.finish()

            raise


execution_manager = ExecutionManager()
