from datetime import datetime


class CompilerLogger:

    def __init__(self):

        self.logs = []

    def log(

        self,

        level,

        message,

    ):

        self.logs.append(

            {

                "time": datetime.now().isoformat(),

                "level": level,

                "message": message,

            }

        )

    def info(self, message):

        self.log(

            "INFO",

            message,

        )

    def warning(self, message):

        self.log(

            "WARNING",

            message,

        )

    def error(self, message):

        self.log(

            "ERROR",

            message,

        )

    def all(self):

        return self.logs.copy()

    def clear(self):

        self.logs.clear()


compiler_logger = CompilerLogger()
