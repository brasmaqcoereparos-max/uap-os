class DeviceManager:

    def __init__(self):
        self.devices = {}

    def register(self, device):
        self.devices[device.id] = device

    def unregister(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]

    def get(self, device_id):
        return self.devices.get(device_id)

    def list(self):
        return list(self.devices.values())

    def connect_all(self):
        for device in self.devices.values():
            if hasattr(device, "connect"):
                device.connect()

    def disconnect_all(self):
        for device in self.devices.values():
            if hasattr(device, "disconnect"):
                device.disconnect()

    def update(self):
        for device in self.devices.values():
            if hasattr(device, "update"):
                device.update()


device_manager = DeviceManager()
