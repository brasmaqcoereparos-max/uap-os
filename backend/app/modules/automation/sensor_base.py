import time

from app.modules.automation.sensor_types import (
    SensorTypes,
)


class SensorBase:
    def __init__(
        self,
        sensor_id,
        name=None,
        sensor_type=SensorTypes.OTHER,
        metadata=None,
    ):
        self.sensor_id = str(sensor_id)

        self.name = (
            str(name)
            if name is not None
            else self.sensor_id
        )

        self.sensor_type = (
            SensorTypes.normalize(
                sensor_type
            )
        )

        self.enabled = False

        self.value = None
        self.previous_value = None

        self.status = "unknown"

        self.last_update = None

        self.metadata = dict(
            metadata or {}
        )

    @property
    def id(self):
        return self.sensor_id

    def enable(self):
        self.enabled = True
        self.status = "ready"

        return True

    def disable(self):
        self.enabled = False
        self.status = "disabled"

        return True

    def update(self, value):
        if not self.enabled:
            return False

        self.previous_value = self.value
        self.value = value

        self.status = "active"
        self.last_update = time.time()

        return value

    def read(self):
        return self.value

    def get_value(self):
        return self.value

    def get_previous_value(self):
        return self.previous_value

    def get_status(self):
        return self.status

    def is_enabled(self):
        return self.enabled

    def has_value(self):
        return self.value is not None

    def reset(self):
        self.value = None
        self.previous_value = None
        self.last_update = None

        self.status = (
            "ready"
            if self.enabled
            else "disabled"
        )

    def to_dict(self):
        return {
            "id": self.sensor_id,
            "name": self.name,
            "type": self.sensor_type,
            "enabled": self.enabled,
            "value": self.value,
            "previous_value": (
                self.previous_value
            ),
            "status": self.status,
            "last_update": (
                self.last_update
            ),
            "metadata": dict(
                self.metadata
            ),
        }
