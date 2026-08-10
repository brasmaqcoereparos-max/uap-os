class AutomationDeviceRegistry:

    def __init__(self):

        self.devices = {}

    def register(
        self,
        device,
    ):

        self.devices[
            device.id
        ] = device

    def unregister(
        self,
        device_id,
    ):

        self.devices.pop(
            device_id,
            None,
        )

    def get(
        self,
        device_id,
    ):

        return self.devices.get(
            device_id
        )

    def list(self):

        return list(
            self.devices.values()
        )


device_registry = AutomationDeviceRegistry()class DeviceRegistry:

    def __init__(self):

        self.devices = {}

    def register(

        self,

        device,

    ):

        self.devices[device.id] = device

    def get(

        self,

        device_id,

    ):

        return self.devices.get(device_id)

    def remove(

        self,

        device_id,

    ):

        self.devices.pop(

            device_id,

            None,

        )

    def all(self):

        return list(self.devices.values())


device_registry = DeviceRegistry()
