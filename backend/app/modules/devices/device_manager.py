from __future__ import annotations

from threading import RLock

from app.modules.uhal.device_model import UniversalDevice


class DeviceManager:
    def __init__(self) -> None:
        self._devices: dict[str, UniversalDevice] = {}
        self._lock = RLock()

    def register(self, device: UniversalDevice) -> UniversalDevice:
        with self._lock:
            self._devices[device.device_id] = device

        return device

    def unregister(self, device_id: str) -> bool:
        with self._lock:
            return self._devices.pop(device_id, None) is not None

    def get(self, device_id: str) -> UniversalDevice | None:
        with self._lock:
            return self._devices.get(device_id)

    def exists(self, device_id: str) -> bool:
        return self.get(device_id) is not None

    def list(self) -> list[UniversalDevice]:
        with self._lock:
            return list(self._devices.values())

    def find_by_type(self, device_type: str) -> list[UniversalDevice]:
        return [
            device
            for device in self.list()
            if device.device_type == device_type
        ]

    def find_by_capability(self, capability: str) -> list[UniversalDevice]:
        return [
            device
            for device in self.list()
            if device.has_capability(capability)
        ]

    def update_state(self, device_id: str, state: str) -> bool:
        device = self.get(device_id)

        if device is None:
            return False

        device.state = state
        return True

    def clear(self) -> None:
        with self._lock:
            self._devices.clear()

    def count(self) -> int:
        with self._lock:
            return len(self._devices)
