import random

from app.modules.simulator.components.virtual_sensor import VirtualSensor


class VirtualTemperature(VirtualSensor):

    def __init__(
        self,
        sensor_id,
        name,
    ):
        super().__init__(
            sensor_id,
            name,
            "TEMPERATURE",
        )

    def update(self):
        self.value = round(
            random.uniform(18, 35),
            1,
        )
