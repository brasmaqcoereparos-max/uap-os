from app.modules.ude.actuator import Actuator


class Motor(Actuator):

    def __init__(
        self,
        name,
        motor_type="dc",
    ):

        super().__init__(
            name,
            "motor",
        )

        self.motor_type = motor_type
        self.speed = 0
        self.direction = 1

    def set_speed(
        self,
        speed,
    ):

        self.speed = speed

    def set_direction(
        self,
        direction,
    ):

        if direction not in (-1, 1):
            raise ValueError(
                "Direction must be -1 or 1"
            )

        self.direction = direction

    def stop(self):

        self.speed = 0
