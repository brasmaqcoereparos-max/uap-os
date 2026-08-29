import time


class VirtualSensor:
    def __init__(
        self,
        sensor_id,
        name,
        sensor_type,
        value=0,
        unit="",
        metadata=None,
    ):
        self.id = str(sensor_id)
        self.sensor_id = self.id

        self.name = str(name)
        self.type = str(
            sensor_type
        )

        self.sensor_type = self.type

        self.value = value
        self.previous_value = None

        self.unit = str(unit)

        self.enabled = True

        self.last_update = None

        self.metadata = dict(
            metadata or {}
        )

    def read(self):
        return self.value

    def set_value(self, value):
        self.previous_value = (
            self.value
        )

        self.value = value

        self.last_update = (
            time.time()
        )

        return value

    def update(self):
        return self.value

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def reset(self, value=0):
        self.previous_value = None
        self.value = value
        self.last_update = None

        return self.value

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "value": self.value,
            "previous_value": (
                self.previous_value
            ),
            "unit": self.unit,
            "enabled": self.enabled,
            "last_update": (
                self.last_update
            ),
            "metadata": dict(
                self.metadata
            ),
        }

    def to_dict(self):
        return self.status()
