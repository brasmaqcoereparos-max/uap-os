from datetime import datetime


class ExecutionTracer:

    def __init__(self):

        self.trace = []

    def enter(
        self,
        node_id,
    ):

        self.trace.append(

            {

                "time": datetime.now().isoformat(),

                "event": "ENTER",

                "node": node_id,

            }

        )

    def leave(
        self,
        node_id,
    ):

        self.trace.append(

            {

                "time": datetime.now().isoformat(),

                "event": "LEAVE",

                "node": node_id,

            }

        )

    def clear(self):

        self.trace.clear()

    def all(self):

        return self.trace


execution_tracer = ExecutionTracer()
