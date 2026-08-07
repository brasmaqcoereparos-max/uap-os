from enum import Enum


class DeviceStatus(Enum):

    OFFLINE = "offline"

    ONLINE = "online"

    READY = "ready"

    RUNNING = "running"

    PAUSED = "paused"

    ERROR = "error"

    DISABLED = "disabled"


class DeviceStatusInfo:

    def __init__(self):

        self.status = DeviceStatus.OFFLINE

        self.message = ""

        self.error_code = None

    def set(
        self,
        status,
        message="",
        error_code=None,
    ):

        self.status = status
        self.message = message
        self.error_code = error_code"""
Universal Device Engine
"""
