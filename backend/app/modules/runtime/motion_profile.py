from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MotionProfile:
    maximum_speed: float = 100.0
    acceleration: float = 50.0
    deceleration: float = 50.0
    current_speed: float = 0.0

    def accelerate(
        self,
        target_speed: float,
        delta_time: float,
    ) -> float:
        target_speed = max(
            0.0,
            min(
                self.maximum_speed,
                float(target_speed),
            ),
        )

        step = self.acceleration * max(
            0.0,
            float(delta_time),
        )

        if self.current_speed < target_speed:
            self.current_speed = min(
                target_speed,
                self.current_speed + step,
            )

        elif self.current_speed > target_speed:
            self.current_speed = max(
                target_speed,
                self.current_speed - step,
            )

        return self.current_speed

    def stop(
        self,
        delta_time: float,
    ) -> float:
        step = self.deceleration * max(
            0.0,
            float(delta_time),
        )

        self.current_speed = max(
            0.0,
            self.current_speed - step,
        )

        return self.current_speed

    def reset(self) -> None:
        self.current_speed = 0.0
