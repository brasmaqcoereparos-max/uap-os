from app.modules.automation.sensor_base import (
    SensorBase,
)

from app.modules.automation.sensor_types import (
    SensorTypes,
)


class ObstacleSensor(SensorBase):

    def __init__(
        self,
        sensor_id,
        name=None,
    ):

        super().__init__(
            sensor_id,
            name,
        )

        self.sensor_type = (
            SensorTypes.OBSTACLE
        )

        self.detected = False

    def detect(self):

        self.detected = True

        self.update(True)

    def clear(self):

        self.detected = False

        self.update(False)

    def is_detected(self):

        return self.detected
