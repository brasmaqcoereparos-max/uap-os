class DeviceConnection:

    def __init__(self):

        self.connected = False

        self.endpoint = None

    def connect(
        self,
        endpoint=None,
    ):

        self.endpoint = endpoint

        self.connected = True

        return True

    def disconnect(self):

        self.connected = False

        self.endpoint = None

    def is_connected(self):

        return self.connected"""
Universal Device Engine
"""
