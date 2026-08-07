from app.modules.ude.device import Device


class Actuator(Device):

    def __init__(
        self,
        name,
        actuator_type,
    ):

        super().__init__(
            name,
            "actuator",
        )

        self.actuator_type = actuator_type
        self.value = 0

    def set(
        self,
        value,
    ):

        self.value = value

    def get(self):

        return self.value
