class DeviceDiagnostics:

    def __init__(self):

        self.messages = []

    def add(
        self,
        level,
        message,
    ):

        self.messages.append(
            {
                "level": level,
                "message": message,
            }
        )

    def clear(self):

        self.messages.clear()

    def all(self):

        return list(
            self.messages
        )"""
Universal Device Engine
"""
