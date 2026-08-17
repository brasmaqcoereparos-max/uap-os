from app.modules.automation.sensor_base import (
    SensorBase,
)

from app.modules.automation.sensor_types import (
    SensorTypes,
)


class DistanceSensor(SensorBase):

    def __init__(
        self,
        sensor_id,
        name=None,
        minimum_distance=0,
        maximum_distance=10000,
    ):

        super().__init__(
            sensor_id,
            name,
        )

        self.sensor_type = (
            SensorTypes.DISTANCE
        )

        self.minimum_distance = (
            minimum_distance
        )

        self.maximum_distance = (
            maximum_distance
        )

        self.distance = None

    def update_distance(
        self,
        distance,
    ):

        if distance < self.minimum_distance:

            distance = self.minimum_distance

        if distance > self.maximum_distance:

            distance = self.maximum_distance

        self.distance = distance

        self.update(distance)

    def get_distance(self):

        return self.distance

    def is_near(
        self,
        threshold,
    ):

        if self.distance is None:
            return False

        return self.distance <= threshold
