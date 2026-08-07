from app.modules.ude.virtual_device import VirtualDevice


class DeviceSimulator:

    def __init__(self):

        self.devices = {}

    def create(
        self,
        name,
    ):

        device = VirtualDevice(name)

        self.devices[device.id] = device

        return device

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

        return list(
            self.devices.values()
        )


device_simulator = DeviceSimulator()"""
Universal Device Engine
"""
