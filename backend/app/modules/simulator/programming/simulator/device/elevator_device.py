"""
Elevador cartesiano/vertical simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ElevatorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="motion",
            description=(
                "Elevador cartesiano "
                "ou vertical"
            ),
            icon="elevator",
        )

        self.level = 0
        self.target_level = 0

        self.minimum_level = 0
        self.maximum_level = None

        self.moving = False
        self.speed = 1

    def move_to(
        self,
        level,
    ):
        if not self.enabled:
            return False

        level = int(level)

        if (
            level
            < self.minimum_level
        ):
            level = self.minimum_level

        if (
            self.maximum_level
            is not None
        ):
            level = min(
                level,
                self.maximum_level,
            )

        self.target_level = level

        self.moving = (
            self.level
            != self.target_level
        )

        return self.target_level

    def set_limits(
        self,
        minimum_level=0,
        maximum_level=None,
    ):
        minimum_level = int(
            minimum_level
        )

        if maximum_level is not None:
            maximum_level = int(
                maximum_level
            )

            if (
                maximum_level
                < minimum_level
            ):
                raise ValueError(
                    "Limites do elevador "
                    "são inválidos."
                )

        self.minimum_level = (
            minimum_level
        )

        self.maximum_level = (
            maximum_level
        )

        return True

    def set_speed(
        self,
        speed,
    ):
        self.speed = max(
            1,
            int(speed),
        )

        return self.speed

    def update(self):
        if (
            not self.enabled
            or not self.moving
        ):
            return self.level

        step = max(
            1,
            int(self.speed),
        )

        if (
            self.level
            < self.target_level
        ):
            self.level = min(
                self.level + step,
                self.target_level,
            )

        elif (
            self.level
            > self.target_level
        ):
            self.level = max(
                self.level - step,
                self.target_level,
            )

        if (
            self.level
            == self.target_level
        ):
            self.moving = False

        return self.level

    def stop(self):
        self.target_level = (
            self.level
        )

        self.moving = False

        return True

    def is_at_target(self):
        return (
            self.level
            == self.target_level
        )

    def reset(self):
        self.level = (
            self.minimum_level
        )

        self.target_level = (
            self.minimum_level
        )

        self.moving = False

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "level": self.level,
            "target_level": (
                self.target_level
            ),
            "minimum_level": (
                self.minimum_level
            ),
            "maximum_level": (
                self.maximum_level
            ),
            "moving": self.moving,
            "speed": self.speed,
        })

        return data
