"""
Universal Device Engine
Classe base de dispositivo.
"""

from uuid import uuid4

from app.modules.ude.device_configuration import (
    DeviceConfiguration,
)

from app.modules.ude.device_status import (
    DeviceStatusInfo,
    DeviceStatus,
)


class Device:

    def __init__(
        self,
        name,
        device_type,
    ):
        self.id = str(uuid4())

        self.name = name
        self.device_type = device_type

        self.enabled = True
        self.connected = False

        self.properties = {}

        self.configuration = (
            DeviceConfiguration()
        )

        self.status = (
            DeviceStatusInfo()
        )

    def connect(self):
        self.connected = True

        self.status.set(
            DeviceStatus.ONLINE
        )

        return True

    def disconnect(self):
        self.connected = False

        self.status.set(
            DeviceStatus.OFFLINE
        )

        return True

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False

        self.status.set(
            DeviceStatus.DISABLED
        )

        return True

    def set_property(
        self,
        name,
        value,
    ):
        self.properties[name] = value

    def get_property(
        self,
        name,
        default=None,
    ):
        return self.properties.get(
            name,
            default,
        )

    def remove_property(
        self,
        name,
    ):
        return self.properties.pop(
            name,
            None,
        )

    def is_available(self):
        return (
            self.enabled
            and self.connected
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "device_type": self.device_type,
            "enabled": self.enabled,
            "connected": self.connected,
            "properties": dict(
                self.properties
            ),
        }
