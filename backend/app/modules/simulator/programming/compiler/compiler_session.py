from uuid import uuid4
from datetime import datetime


class CompilerSession:

    def __init__(self):

        self.id = str(uuid4())

        self.started = datetime.now()

        self.finished = None

    def finish(self):

        self.finished = datetime.now()

    def to_dict(self):

        return {

            "id": self.id,

            "started": self.started.isoformat(),

            "finished": (

                self.finished.isoformat()

                if self.finished

                else None

            ),

        }


compiler_session = CompilerSession()
