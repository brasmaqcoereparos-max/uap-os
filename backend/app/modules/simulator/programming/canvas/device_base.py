class DeviceBase:

    def __init__(self, name):

        self.name = name

        self.enabled = True

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def status(self):

        return {
            "name": self.name,
            "enabled": self.enabled,
            "connected": self.connected,
        }
