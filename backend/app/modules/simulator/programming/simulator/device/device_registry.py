"""
Registro das instâncias de dispositivos UAP.
"""


class DeviceRegistry:
    def __init__(self):
        self._devices = {}

    @staticmethod
    def _device_name(device):
        return getattr(
            device,
            "name",
            None,
        )

    def register(
        self,
        name,
        device=None,
        replace=True,
    ):
        if device is None:
            device = name
            name = self._device_name(
                device
            )

        if not name:
            raise ValueError(
                "Nome do dispositivo "
                "é obrigatório."
            )

        key = str(name)

        if (
            key in self._devices
            and not replace
        ):
            raise ValueError(
                "Instância já "
                f"registrada: {key}"
            )

        self._devices[
            key
        ] = device

        return device

    def get(self, name):
        return self._devices.get(
            str(name)
        )

    def exists(self, name):
        return (
            str(name)
            in self._devices
        )

    def unregister(self, name):
        return self._devices.pop(
            str(name),
            None,
        )

    def all(self):
        return self._devices.copy()

    def values(self):
        return list(
            self._devices.values()
        )

    def names(self):
        return list(
            self._devices.keys()
        )

    def count(self):
        return len(self._devices)

    def clear(self):
        count = self.count()

        self._devices.clear()

        return count


device_registry = DeviceRegistry()
