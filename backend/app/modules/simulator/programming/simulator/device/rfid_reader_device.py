"""
Leitor RFID simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class RFIDReaderDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="reader",
            description="Leitor RFID",
            icon="rfid",
        )

        self.uid = None
        self.last_uid = None

        self.data = {}

        self.scan_count = 0

    def scan(
        self,
        uid,
    ):
        if not self.enabled:
            return False

        if uid is None:
            return None

        self.uid = str(uid)
        self.last_uid = self.uid

        self.scan_count += 1

        return self.uid

    def read_uid(self):
        return self.uid

    def has_tag(self):
        return self.uid is not None

    def write_data(
        self,
        key,
        value,
    ):
        if self.uid is None:
            return False

        self.data[
            str(key)
        ] = value

        return value

    def read_data(
        self,
        key,
    ):
        return self.data.get(
            str(key)
        )

    def remove_data(
        self,
        key,
    ):
        return self.data.pop(
            str(key),
            None,
        )

    def clear_tag(self):
        self.uid = None

        return True

    def clear(self):
        self.uid = None
        self.last_uid = None
        self.data.clear()

        return True

    def update(self):
        return self.uid

    def reset(self):
        self.uid = None
        self.last_uid = None
        self.data.clear()
        self.scan_count = 0

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "uid": self.uid,
            "last_uid": (
                self.last_uid
            ),
            "data": dict(
                self.data
            ),
            "scan_count": (
                self.scan_count
            ),
        })

        return data
