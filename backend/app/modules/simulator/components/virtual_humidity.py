import random

from app.modules.simulator.components.virtual_sensor import VirtualSensor


class VirtualHumidity(VirtualSensor):

    def __init__(
        self,
        sensor_id,
        name,
    ):
        super().__init__(
            sensor_id,
            name,
            "HUMIDITY",
        )

    def update(self):
        self.value = random.randint(
            20,
            90,
        )
