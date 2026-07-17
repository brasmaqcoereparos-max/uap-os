from uuid import uuid4
from datetime import datetime


class ExecutionSession:

    def __init__(self):

        self.id = str(uuid4())

        self.started = datetime.now()

        self.finished = None

        self.status = "idle"

    def start(self):

        self.status = "running"

    def finish(self):

        self.status = "finished"

        self.finished = datetime.now()

    def error(self):

        self.status = "error"

        self.finished = datetime.now()

    def to_dict(self):

        return {

            "id": self.id,

            "status": self.status,

            "started": self.started.isoformat(),

            "finished": (
                self.finished.isoformat()
                if self.finished
                else None
            ),

        }


execution_session = ExecutionSession()
