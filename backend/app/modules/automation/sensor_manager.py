from app.modules.automation.sensor_registry import (
    sensor_registry,
)

from app.modules.automation.sensor_base import (
    SensorBase,
)

from app.modules.automation.sensor_state import (
    sensor_state,
)

from app.modules.automation.sensor_types import (
    SensorTypes,
)


class SensorManager:
    def create(
        self,
        sensor_id,
        name=None,
        sensor_type=SensorTypes.OTHER,
        metadata=None,
        replace=True,
    ):
        sensor = SensorBase(
            sensor_id=sensor_id,
            name=name,
            sensor_type=sensor_type,
            metadata=metadata,
        )

        sensor_registry.register(
            sensor.sensor_id,
            sensor,
            replace=replace,
        )

        return sensor

    def register(
        self,
        sensor,
        replace=True,
    ):
        sensor_id = getattr(
            sensor,
            "sensor_id",
            getattr(
                sensor,
                "id",
                None,
            ),
        )

        if sensor_id is None:
            raise ValueError(
                "Sensor sem identificador."
            )

        return sensor_registry.register(
            sensor_id,
            sensor,
            replace=replace,
        )

    def remove(self, sensor_id):
        sensor_state.remove(
            sensor_id
        )

        return sensor_registry.unregister(
            sensor_id
        )

    def get(self, sensor_id):
        return sensor_registry.get(
            sensor_id
        )

    def get_all(self):
        return sensor_registry.get_all()

    def enable(self, sensor_id):
        sensor = self.get(sensor_id)

        if sensor is None:
            return False

        result = sensor.enable()

        sensor_state.update(
            sensor_id,
            sensor.get_value(),
            active=True,
            status=sensor.get_status(),
        )

        return result

    def disable(self, sensor_id):
        sensor = self.get(sensor_id)

        if sensor is None:
            return False

        result = sensor.disable()

        sensor_state.deactivate(
            sensor_id
        )

        return result

    def update(
        self,
        sensor_id,
        value,
    ):
        sensor = self.get(sensor_id)

        if sensor is None:
            return False

        result = sensor.update(value)

        if result is False:
            return False

        sensor_state.update(
            sensor_id,
            value,
            active=True,
            status=sensor.get_status(),
        )

        return result

    def read(
        self,
        sensor_id,
        default=None,
    ):
        sensor = self.get(sensor_id)

        if sensor is None:
            return default

        reader = getattr(
            sensor,
            "read",
            None,
        )

        if callable(reader):
            return reader()

        getter = getattr(
            sensor,
            "get_value",
            None,
        )

        if callable(getter):
            return getter()

        return default

    def enabled(self):
        return [
            sensor
            for sensor
            in sensor_registry.all()
            if getattr(
                sensor,
                "enabled",
                False,
            )
        ]

    def count(self):
        return sensor_registry.count()


sensor_manager = SensorManager()
