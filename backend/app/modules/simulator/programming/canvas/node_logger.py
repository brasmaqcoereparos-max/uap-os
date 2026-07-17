from datetime import datetime


class NodeLogger:

    def __init__(self):

        self.logs = []

    def log(
        self,
        level,
        node_id,
        message,
    ):

        self.logs.append(

            {

                "time": datetime.now().isoformat(),

                "level": level,

                "node": node_id,

                "message": message,

            }

        )

    def clear(self):

        self.logs.clear()

    def all(self):

        return self.logs

    def errors(self):

        return [

            log

            for log

            in self.logs

            if log["level"] == "ERROR"

        ]


node_logger = NodeLogger()
