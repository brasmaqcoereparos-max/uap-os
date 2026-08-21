"""
Catálogo de classes de dispositivos do UAP.
"""

from typing import Dict, Type

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class DeviceCatalog:

    def __init__(self):

        self._devices: Dict[
            str,
            Type[DeviceBase],
        ] = {}

    def register(
        self,
        name: str,
        device_class: Type[DeviceBase],
    ):

        if not name:
            raise ValueError(
                "O nome do dispositivo é obrigatório."
            )

        self._devices[
            name.upper()
        ] = device_class

        return device_class

    def get(
        self,
        name: str,
    ):

        if not name:
            return None

        return self._devices.get(
            name.upper()
        )

    def exists(
        self,
        name: str,
    ):

        return self.get(name) is not None

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

    def unregister(
        self,
        name: str,
    ):

        if not name:
            return None

        return self._devices.pop(
            name.upper(),
            None,
        )

    def clear(self):

        self._devices.clear()


device_catalog = DeviceCatalog()
