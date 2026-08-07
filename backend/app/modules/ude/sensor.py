from app.modules.ude.device import Device


class Sensor(Device):

    def __init__(
        self,
        name,
        sensor_type,
    ):

        super().__init__(
            name,
            "sensor",
        )

        self.sensor_type = sensor_type
        self.value = None

    def update(
        self,
        value,
    ):

        self.value = value

    def read(self):

        return self.value
