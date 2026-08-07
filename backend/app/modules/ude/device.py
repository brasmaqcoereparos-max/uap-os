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

    def disconnect(self):

        self.connected = False

        self.status.set(
            DeviceStatus.OFFLINE
        )

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

        self.status.set(
            DeviceStatus.DISABLED
        )

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
        )from uuid import uuid4


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

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False"""
Universal Device Engine
"""
