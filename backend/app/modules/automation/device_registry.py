"""
Registro de dispositivos da camada de automação.
"""

from typing import Any


class AutomationDeviceRegistry:
    def __init__(self):
        self._devices: dict[
            str,
            Any,
        ] = {}

    def register(
        self,
        device_id: str,
        device: Any,
        replace: bool = True,
    ):
        device_id = str(
            device_id
        )

        if (
            device_id
            in self._devices
            and not replace
        ):
            raise ValueError(
                "Dispositivo já registrado: "
                f"{device_id}"
            )

        self._devices[
            device_id
        ] = device

        return device

    def unregister(
        self,
        device_id: str,
    ):
        return self._devices.pop(
            str(device_id),
            None,
        )

    def get(
        self,
        device_id: str,
    ):
        return self._devices.get(
            str(device_id)
        )

    def list(self):
        return list(
            self._devices.values()
        )

    def all(self):
        return self.list()

    def ids(self):
        return list(
            self._devices.keys()
        )

    def exists(
        self,
        device_id: str,
    ):
        return (
            str(device_id)
            in self._devices
        )

    def count(self):
        return len(
            self._devices
        )

    def clear(self):
        count = self.count()
        self._devices.clear()

        return count

    def to_dict(self):
        return {
            device_id: (
                device.to_dict()
                if hasattr(
                    device,
                    "to_dict",
                )
                else str(device)
            )
            for device_id, device
            in self._devices.items()
        }


device_registry = (
    AutomationDeviceRegistry()
    )
