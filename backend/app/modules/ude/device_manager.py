class DeviceManager:

    def __init__(self):

        self.devices = {}

    def add(

        self,

        device,

    ):

        self.devices[device.id] = device

    def remove(

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

            device_id,

        )

    def list(self):

        return list(

            self.devices.values(),

        )


device_manager = DeviceManager()"""
Universal Device Engine
"""
