class CompilerReport:

    def __init__(self):

        self.messages = []

    def info(self, message):

        self.messages.append(

            {

                "type": "info",

                "message": message,

            }

        )

    def warning(self, message):

        self.messages.append(

            {

                "type": "warning",

                "message": message,

            }

        )

    def error(self, message):

        self.messages.append(

            {

                "type": "error",

                "message": message,

            }

        )

    def all(self):

        return self.messages.copy()


compiler_report = CompilerReport()
