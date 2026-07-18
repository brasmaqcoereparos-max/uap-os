from app.modules.simulator.programming.canvas.device_base import DeviceBase


class DeviceManager:

    def __init__(self):

        self.devices = {}

    def register(self, device: DeviceBase):

        self.devices[device.name] = device

    def remove(self, name):

        self.devices.pop(name, None)

    def get(self, name):

        return self.devices.get(name)

    def connect(self, name):

        device = self.get(name)

        if device:

            device.connect()

    def disconnect(self, name):

        device = self.get(name)

        if device:

            device.disconnect()

    def clear(self):

        self.devices.clear()

    def all(self):

        return {

            name: device.status()

            for name, device

            in self.devices.items()

        }


device_manager = DeviceManager()
