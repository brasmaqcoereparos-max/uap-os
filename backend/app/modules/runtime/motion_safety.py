from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MotionLimits:
    maximum_speed: float = 100.0
    minimum_speed: float = 0.0
    emergency_stop: bool = False
    enabled: bool = True


class MotionSafetyManager:
    def __init__(
        self,
        limits: MotionLimits | None = None,
    ) -> None:
        self.limits = limits or MotionLimits()

    def validate_speed(
        self,
        speed: float,
    ) -> float:
        if not self.limits.enabled:
            raise RuntimeError(
                "Motion safety system disabled"
            )

        if self.limits.emergency_stop:
            raise RuntimeError(
                "Emergency stop is active"
            )

        return max(
            self.limits.minimum_speed,
            min(
                self.limits.maximum_speed,
                float(speed),
            ),
        )

    def activate_emergency_stop(self) -> None:
        self.limits.emergency_stop = True

    def reset_emergency_stop(self) -> None:
        self.limits.emergency_stop = False

    def disable_motion(self) -> None:
        self.limits.enabled = False

    def enable_motion(self) -> None:
        self.limits.enabled = True
