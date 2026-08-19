from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Servo:
    servo_id: str
    name: str
    device_id: str | None = None
    angle: float = 90.0
    minimum: float = 0.0
    maximum: float = 180.0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def set_angle(self, angle: float) -> None:
        self.angle = max(
            self.minimum,
            min(self.maximum, float(angle)),
        )


class ServoManager:
    def __init__(self) -> None:
        self._servos: dict[str, Servo] = {}

    def register(
        self,
        servo_id: str,
        name: str,
        device_id: str | None = None,
        minimum: float = 0.0,
        maximum: float = 180.0,
        metadata: dict[str, Any] | None = None,
    ) -> Servo:
        servo = Servo(
            servo_id=servo_id,
            name=name,
            device_id=device_id,
            minimum=minimum,
            maximum=maximum,
            metadata=metadata or {},
        )

        servo.set_angle(
            (minimum + maximum) / 2
        )

        self._servos[servo_id] = servo
        return servo

    def get(self, servo_id: str) -> Servo | None:
        return self._servos.get(servo_id)

    def list(self) -> list[Servo]:
        return list(self._servos.values())

    def set_angle(
        self,
        servo_id: str,
        angle: float,
    ) -> Servo:
        servo = self.get(servo_id)

        if servo is None:
            raise KeyError(f"Servo '{servo_id}' not found")

        servo.set_angle(angle)
        return servo

    def remove(self, servo_id: str) -> bool:
        return self._servos.pop(
            servo_id,
            None,
        ) is not None
