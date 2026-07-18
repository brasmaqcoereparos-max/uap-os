from datetime import datetime


class DeviceLogger:

    def __init__(self):

        self.logs = []

    def log(

        self,

        device,

        level,

        message,

    ):

        self.logs.append(

            {

                "time": datetime.now().isoformat(),

                "device": device,

                "level": level,

                "message": message,

            }

        )

    def clear(self):

        self.logs.clear()

    def all(self):

        return self.logs.copy()

    def errors(self):

        return [

            log

            for log in self.logs

            if log["level"] == "ERROR"

        ]


device_logger = DeviceLogger()
