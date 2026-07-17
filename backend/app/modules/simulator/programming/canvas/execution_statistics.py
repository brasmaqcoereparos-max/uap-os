from datetime import datetime


class ExecutionStatistics:

    def __init__(self):

        self.reset()

    def reset(self):

        self.started = datetime.now()

        self.finished = None

        self.executed = 0

        self.errors = 0

    def node_executed(self):

        self.executed += 1

    def node_error(self):

        self.errors += 1

    def finish(self):

        self.finished = datetime.now()

    def to_dict(self):

        return {

            "started": self.started.isoformat(),

            "finished": self.finished.isoformat() if self.finished else None,

            "executed": self.executed,

            "errors": self.errors,

            "success_rate": (

                100

                if self.executed == 0

                else round(

                    ((self.executed - self.errors) / self.executed) * 100,

                    2,

                )

            ),

        }


execution_statistics = ExecutionStatistics()
