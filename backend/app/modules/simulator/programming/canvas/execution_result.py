from datetime import datetime


class ExecutionResult:

    def __init__(self):

        self.success = True

        self.started = datetime.now()

        self.finished = None

        self.executed = []

        self.errors = []

    def add_node(
        self,
        node_id,
    ):

        self.executed.append(node_id)

    def add_error(
        self,
        node_id,
        message,
    ):

        self.success = False

        self.errors.append(

            {

                "node": node_id,

                "message": message,

            }

        )

    def finish(self):

        self.finished = datetime.now()

    def to_dict(self):

        return {

            "success": self.success,

            "started": self.started.isoformat(),

            "finished": self.finished.isoformat() if self.finished else None,

            "executed": self.executed,

            "errors": self.errors,

        }


execution_result = ExecutionResult()
