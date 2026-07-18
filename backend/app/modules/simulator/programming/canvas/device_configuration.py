class DeviceConfiguration:

    def __init__(self):

        self.config = {}

    def set(self, device, values):

        self.config[device] = values

    def update(self, device, values):

        self.config.setdefault(device, {})
        self.config[device].update(values)

    def get(self, device):

        return self.config.get(device, {})

    def remove(self, device):

        self.config.pop(device, None)

    def clear(self):

        self.config.clear()


device_configuration = DeviceConfiguration()
