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
        self._devices[name] = device_class
        return device_class

    def get(
        self,
        name: str,
    ):
        return self._devices.get(name)

    def exists(
        self,
        name: str,
    ):
        return name in self._devices

    def all(self):
        return self._devices.copy()

    def count(self):
        return len(self._devices)

    def unregister(
        self,
        name: str,
    ):
        return self._devices.pop(
            name,
            None,
        )

    def clear(self):
        self._devices.clear()


device_catalog = DeviceCatalog()
