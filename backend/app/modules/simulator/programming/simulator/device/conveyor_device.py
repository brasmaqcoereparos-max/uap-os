"""
Esteira transportadora simulada do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ConveyorDevice(DeviceBase):

    FORWARD = "forward"
    REVERSE = "reverse"

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="motion",
            description=(
                "Esteira transportadora"
            ),
            icon="conveyor",
        )

        self.running = False
        self.speed = 0

        self.direction = (
            self.FORWARD
        )

        self.distance = 0.0

    def start(
        self,
        speed=100,
    ):
        if not self.enabled:
            return False

        self.speed = max(
            0,
            min(
                100,
                int(speed),
            ),
        )

        self.running = (
            self.speed > 0
        )

        return self.speed

    def stop(self):
        self.running = False
        self.speed = 0

        return True

    def set_speed(
        self,
        speed,
    ):
        return self.start(speed)

    def set_direction(
        self,
        direction,
    ):
        value = str(
            direction
        ).strip().lower()

        if value not in {
            self.FORWARD,
            self.REVERSE,
        }:
            raise ValueError(
                "Direção inválida: "
                f"{direction}"
            )

        self.direction = value

        return self.direction

    def reverse(self):
        if (
            self.direction
            == self.FORWARD
        ):
            self.direction = (
                self.REVERSE
            )
        else:
            self.direction = (
                self.FORWARD
            )

        return self.direction

    def update(self):
        if (
            self.enabled
            and self.running
        ):
            delta = (
                float(self.speed)
                / 100.0
            )

            if (
                self.direction
                == self.REVERSE
            ):
                delta *= -1

            self.distance += delta

        return self.distance

    def reset(self):
        self.stop()

        self.direction = (
            self.FORWARD
        )

        self.distance = 0.0

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "running": self.running,
            "speed": self.speed,
            "direction": (
                self.direction
            ),
            "distance": (
                self.distance
            ),
        })

        return data
