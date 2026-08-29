from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class StepperMotorDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="motion",
            description=(
                "Motor de passo"
            ),
            icon="stepper",
        )

        self.position = 0
        self.target_position = 0

        self.speed = 0
        self.moving = False

    def move(
        self,
        steps,
        speed=100,
    ):
        if not self.enabled:
            return False

        self.target_position = (
            self.position
            + int(steps)
        )

        self.speed = max(
            0,
            int(speed),
        )

        self.moving = (
            self.position
            != self.target_position
        )

        return self.target_position

    def move_to(
        self,
        position,
        speed=100,
    ):
        if not self.enabled:
            return False

        self.target_position = int(
            position
        )

        self.speed = max(
            0,
            int(speed),
        )

        self.moving = (
            self.position
            != self.target_position
        )

        return self.target_position

    def stop(self):
        self.target_position = (
            self.position
        )

        self.moving = False
        self.speed = 0

        return True

    def update(self):
        if (
            not self.enabled
            or not self.moving
        ):
            return self.position

        if (
            self.position
            < self.target_position
        ):
            self.position += 1

        elif (
            self.position
            > self.target_position
        ):
            self.position -= 1

        if (
            self.position
            == self.target_position
        ):
            self.moving = False
            self.speed = 0

        return self.position

    def reset(self):
        self.position = 0
        self.target_position = 0
        self.speed = 0
        self.moving = False

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "position": self.position,
            "target_position": (
                self.target_position
            ),
            "speed": self.speed,
            "moving": self.moving,
        })

        return data
