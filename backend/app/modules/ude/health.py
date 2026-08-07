class DeviceHealth:

    def __init__(self):

        self.online = False

        self.last_error = None

        self.last_check = None

    def update(
        self,
        online,
        error=None,
    ):

        self.online = online

        self.last_error = error

    def is_healthy(self):

        return (
            self.online
            and self.last_error is None
        )"""
Universal Device Engine
"""
