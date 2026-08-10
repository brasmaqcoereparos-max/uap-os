from enum import Enum


class AlarmLevel(Enum):

    INFO = "info"

    WARNING = "warning"

    CRITICAL = "critical"


class DeviceAlarm:

    def __init__(
        self,
        name,
        level=AlarmLevel.WARNING,
        message="",
    ):

        self.name = name
        self.level = level
        self.message = message
        self.active = False

    def activate(self):

        self.active = True

    def deactivate(self):

        self.active = False
