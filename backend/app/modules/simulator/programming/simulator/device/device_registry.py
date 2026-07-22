class DeviceRegistry:

    def __init__(self):

        self.devices = {}

    def register(

        self,

        name,

        device,

    ):

        self.devices[name] = device

    def get(

        self,

        name,

    ):

        return self.devices.get(

            name,

        )

    def all(self):

        return self.devices.copy()

    def clear(self):

        self.devices.clear()


device_registry = DeviceRegistry()
