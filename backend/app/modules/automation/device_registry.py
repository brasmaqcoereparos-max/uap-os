"""
Registro de dispositivos da camada de automação.
"""

from typing import Any


class AutomationDeviceRegistry:

    def __init__(self):
        self._devices: dict[str, Any] = {}

    def register(
        self,
        device_id: str,
        device: Any,
    ):
        self._devices[device_id] = device
        return device

    def unregister(
        self,
        device_id: str,
    ):
        return self._devices.pop(
            device_id,
            None,
        )

    def get(
        self,
        device_id: str,
    ):
        return self._devices.get(
            device_id
        )

    def list(self):
        return list(
            self._devices.values()
        )

    def ids(self):
        return list(
            self._devices.keys()
        )

    def exists(
        self,
        device_id: str,
    ):
        return device_id in self._devices

    def clear(self):
        self._devices.clear()


device_registry = AutomationDeviceRegistry()
