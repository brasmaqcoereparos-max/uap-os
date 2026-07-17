class ExecutionDevices:

    def __init__(self):

        self.devices = {}

    def register(
        self,
        name,
        device,
    ):

        self.devices[name] = device

    def unregister(
        self,
        name,
    ):

        self.devices.pop(name, None)

    def get(
        self,
        name,
    ):

        return self.devices.get(name)

    def exists(
        self,
        name,
    ):

        return name in self.devices

    def clear(self):

        self.devices.clear()

    def all(self):

        return self.devices.copy()


execution_devices = ExecutionDevices()
