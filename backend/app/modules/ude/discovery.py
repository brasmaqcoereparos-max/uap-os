class DeviceDiscovery:

    def __init__(self):

        self.discovered = {}

    def add(
        self,
        device,
    ):

        self.discovered[device.id] = device

    def remove(
        self,
        device_id,
    ):

        self.discovered.pop(
            device_id,
            None,
        )

    def find(
        self,
        device_type=None,
    ):

        devices = list(
            self.discovered.values()
        )

        if device_type is None:
            return devices

        return [
            device
            for device in devices
            if device.device_type == device_type
        ]

    def all(self):

        return list(
            self.discovered.values()
        )


device_discovery = DeviceDiscovery()"""
Universal Device Engine
"""
