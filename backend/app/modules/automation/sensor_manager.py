from app.modules.automation.sensor_registry import (
    sensor_registry,
)

from app.modules.automation.sensor_base import (
    SensorBase,
)


class SensorManager:

    def create(
        self,
        sensor_id,
        name=None,
    ):

        sensor = SensorBase(
            sensor_id,
            name,
        )

        sensor_registry.register(
            sensor_id,
            sensor,
        )

        return sensor

    def register(
        self,
        sensor,
    ):

        sensor_registry.register(
            sensor.sensor_id,
            sensor,
        )

        return sensor

    def remove(
        self,
        sensor_id,
    ):

        return sensor_registry.unregister(
            sensor_id
        )

    def get(
        self,
        sensor_id,
    ):

        return sensor_registry.get(
            sensor_id
        )

    def get_all(self):

        return sensor_registry.get_all()

    def enable(
        self,
        sensor_id,
    ):

        sensor = self.get(sensor_id)

        if sensor is None:
            return False

        sensor.enable()

        return True

    def disable(
        self,
        sensor_id,
    ):

        sensor = self.get(sensor_id)

        if sensor is None:
            return False

        sensor.disable()

        return True


sensor_manager = SensorManager()
