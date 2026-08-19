from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Motor:
    motor_id: str
    name: str
    motor_type: str = "dc"
    device_id: str | None = None
    speed: float = 0.0
    direction: int = 0
    enabled: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def set_speed(self, speed: float) -> None:
        self.speed = max(0.0, min(100.0, float(speed)))

    def set_direction(self, direction: int) -> None:
        if direction not in (-1, 0, 1):
            raise ValueError("Direction must be -1, 0 or 1")

        self.direction = direction

    def start(self, speed: float | None = None) -> None:
        if speed is not None:
            self.set_speed(speed)

        self.enabled = True

        if self.direction == 0:
            self.direction = 1

    def stop(self) -> None:
        self.enabled = False
        self.speed = 0.0
        self.direction = 0


class MotorManager:
    def __init__(self) -> None:
        self._motors: dict[str, Motor] = {}

    def register(
        self,
        motor_id: str,
        name: str,
        motor_type: str = "dc",
        device_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Motor:
        motor = Motor(
            motor_id=motor_id,
            name=name,
            motor_type=motor_type,
            device_id=device_id,
            metadata=metadata or {},
        )

        self._motors[motor_id] = motor
        return motor

    def get(self, motor_id: str) -> Motor | None:
        return self._motors.get(motor_id)

    def list(self) -> list[Motor]:
        return list(self._motors.values())

    def start(
        self,
        motor_id: str,
        speed: float | None = None,
    ) -> Motor:
        motor = self.get(motor_id)

        if motor is None:
            raise KeyError(f"Motor '{motor_id}' not found")

        motor.start(speed)
        return motor

    def stop(self, motor_id: str) -> Motor:
        motor = self.get(motor_id)

        if motor is None:
            raise KeyError(f"Motor '{motor_id}' not found")

        motor.stop()
        return motor

    def set_speed(
        self,
        motor_id: str,
        speed: float,
    ) -> Motor:
        motor = self.get(motor_id)

        if motor is None:
            raise KeyError(f"Motor '{motor_id}' not found")

        motor.set_speed(speed)
        return motor

    def set_direction(
        self,
        motor_id: str,
        direction: int,
    ) -> Motor:
        motor = self.get(motor_id)

        if motor is None:
            raise KeyError(f"Motor '{motor_id}' not found")

        motor.set_direction(direction)
        return motor

    def remove(self, motor_id: str) -> bool:
        return self._motors.pop(motor_id, None) is not None
