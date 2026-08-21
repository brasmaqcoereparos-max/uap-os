"""
Universal Device Engine
Estado operacional dos dispositivos.
"""

from enum import Enum


class DeviceStatus(str, Enum):
    UNKNOWN = "unknown"
    OFFLINE = "offline"
    ONLINE = "online"
    BUSY = "busy"
    ERROR = "error"
    DISABLED = "disabled"
    MAINTENANCE = "maintenance"


class DeviceStatusInfo:

    def __init__(
        self,
        status: DeviceStatus = DeviceStatus.UNKNOWN,
        message: str = "",
    ):
        self.status = status
        self.message = message

    def set(
        self,
        status: DeviceStatus,
        message: str = "",
    ):
        self.status = status
        self.message = message

    def is_online(self):
        return self.status == DeviceStatus.ONLINE

    def is_error(self):
        return self.status == DeviceStatus.ERROR

    def is_available(self):
        return self.status == DeviceStatus.ONLINE

    def to_dict(self):
        return {
            "status": self.status.value,
            "message": self.message,
        }
