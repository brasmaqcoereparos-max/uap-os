from datetime import datetime


class ExecutionEvents:

    def __init__(self):

        self.events = []

    def emit(
        self,
        event,
        node_id=None,
        payload=None,
    ):

        self.events.append(

            {

                "time": datetime.now().isoformat(),

                "event": event,

                "node": node_id,

                "payload": payload,

            }

        )

    def clear(self):

        self.events.clear()

    def all(self):

        return self.events.copy()


execution_events = ExecutionEvents()
