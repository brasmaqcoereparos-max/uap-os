class DeviceGroup:

    def __init__(

        self,

        name,

    ):

        self.name = name

        self.devices = []

    def add(

        self,

        device,

    ):

        self.devices.append(device)

    def remove(

        self,

        device,

    ):

        if device in self.devices:

            self.devices.remove(device)

    def all(self):

        return self.devices.copy()
