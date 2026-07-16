import random

from app.modules.simulator.components.virtual_sensor import VirtualSensor


class VirtualUltrasonic(VirtualSensor):

    def __init__(
        self,
        sensor_id,
        name,
    ):
        super().__init__(
            sensor_id,
            name,
            "ULTRASONIC",
        )

    def update(self):
        self.value = round(
            random.uniform(5, 400),
            2,
        )
