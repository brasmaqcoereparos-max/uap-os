"""
Registro das instâncias de dispositivos do UAP.
"""


class DeviceRegistry:

    def __init__(self):

        self._devices = {}

    def register(
        self,
        name,
        device,
    ):

        if not name:
            raise ValueError(
                "O nome do dispositivo é obrigatório."
            )

        self._devices[name] = device

        return device

    def get(
        self,
        name,
    ):

        return self._devices.get(
            name
        )

    def exists(
        self,
        name,
    ):

        return name in self._devices

    def unregister(
        self,
        name,
    ):

        return self._devices.pop(
            name,
            None,
        )

    def all(self):

        return self._devices.copy()

    def names(self):

        return list(
            self._devices.keys()
        )

    def count(self):

        return len(
            self._devices
        )

    def clear(self):

        self._devices.clear()


device_registry = DeviceRegistry()
