class VirtualWorld:

    def __init__(self):

        self.devices = []

    def add(

        self,

        device,

    ):

        self.devices.append(device)

    def update(self):

        for device in self.devices:

            device.update()

    def reset(self):

        for device in self.devices:

            device.reset()


virtual_world = VirtualWorld()
