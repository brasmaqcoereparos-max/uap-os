"""
Sensor virtual base do simulador UAP.
"""

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
        self.id = str(
            sensor_id
        )

        self.sensor_id = (
            self.id
        )

        self.name = str(
            name
        )

        self.type = str(
            sensor_type
        )

        self.sensor_type = (
            self.type
        )

        self.value = value
        self.previous_value = None

        self.unit = str(
            unit
        )

        self.enabled = True

        self.last_update = None

        self.metadata = dict(
            metadata or {}
        )

        self.read_count = 0
        self.update_count = 0

        self.minimum_observed = None
        self.maximum_observed = None

    def read(self):
        self.read_count += 1

        return self.value

    def _track_value(
        self,
        value,
    ):
        if isinstance(
            value,
            (int, float),
        ):
            if (
                self.minimum_observed
                is None
                or value
                < self.minimum_observed
            ):
                self.minimum_observed = value

            if (
                self.maximum_observed
                is None
                or value
                > self.maximum_observed
            ):
                self.maximum_observed = value

    def set_value(
        self,
        value,
    ):
        self.previous_value = (
            self.value
        )

        self.value = value

        self.last_update = (
            time.time()
        )

        self._track_value(
            value
        )

        return value

    def update(self):
        if not self.enabled:
            return self.value

        self.update_count += 1

        return self.value

    def enable(self):
        self.enabled = True

        return self

    def disable(self):
        self.enabled = False

        return self

    def reset(
        self,
        value=0,
    ):
        self.previous_value = None

        self.value = value
        self.last_update = None

        self.read_count = 0
        self.update_count = 0

        self.minimum_observed = None
        self.maximum_observed = None

        return self.value

    def set_metadata(
        self,
        key,
        value,
    ):
        self.metadata[
            str(key)
        ] = value

        return value

    def get_metadata(
        self,
        key,
        default=None,
    ):
        return self.metadata.get(
            str(key),
            default,
        )

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
            "enabled": (
                self.enabled
            ),
            "last_update": (
                self.last_update
            ),
            "metadata": dict(
                self.metadata
            ),
        }

    def detailed_status(self):
        return {
            **self.status(),
            "read_count": (
                self.read_count
            ),
            "update_count": (
                self.update_count
            ),
            "minimum_observed": (
                self.minimum_observed
            ),
            "maximum_observed": (
                self.maximum_observed
            ),
        }

    def to_dict(self):
        return self.status()
