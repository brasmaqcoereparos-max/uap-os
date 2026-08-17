class CleaningActuator:

    def __init__(
        self,
        actuator_id,
        name,
    ):

        self.actuator_id = actuator_id
        self.name = name
        self.enabled = False
        self.power = 0

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False
        self.power = 0

    def set_power(self, power):

        self.power = max(
            0,
            min(100, power),
        )

    def is_enabled(self):

        return self.enabled

    def get_power(self):

        return self.power

    def to_dict(self):

        return {
            "id": self.actuator_id,
            "name": self.name,
            "enabled": self.enabled,
            "power": self.power,
        }
