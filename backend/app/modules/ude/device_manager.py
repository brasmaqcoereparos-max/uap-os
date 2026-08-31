"""
Universal Device Engine
Gerenciador de dispositivos.
"""

from app.modules.ude.device import (
    Device,
)


class DeviceManager:

    def __init__(self):
        self.devices = {}

    def add(
        self,
        device: Device,
    ):
        self.devices[
            device.id
        ] = device

        return device

    def create(
        self,
        name,
        device_type,
    ):
        device = Device(
            name=name,
            device_type=device_type,
        )

        return self.add(
            device
        )

    def get(
        self,
        device_id,
    ):
        return self.devices.get(
            device_id
        )

    def remove(
        self,
        device_id,
    ):
        return self.devices.pop(
            device_id,
            None,
        )

    def list(self):
        return list(
            self.devices.values()
        )

    def connect(
        self,
        device_id,
    ):
        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Device "
                f"'{device_id}' "
                f"not found"
            )

        return device.connect()

    def disconnect(
        self,
        device_id,
    ):
        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Device "
                f"'{device_id}' "
                f"not found"
            )

        return device.disconnect()

    def enable(
        self,
        device_id,
    ):
        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Device "
                f"'{device_id}' "
                f"not found"
            )

        return device.enable()

    def disable(
        self,
        device_id,
    ):
        device = self.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Device "
                f"'{device_id}' "
                f"not found"
            )

        return device.disable()

    def clear(self):
        self.devices.clear()


device_manager = DeviceManager()
