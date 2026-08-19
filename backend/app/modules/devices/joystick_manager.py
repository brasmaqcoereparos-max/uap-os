from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class JoystickState:
    joystick_id: str
    name: str
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    throttle: float = 0.0
    buttons: dict[str, bool] = field(default_factory=dict)
    hats: dict[str, tuple[int, int]] = field(default_factory=dict)
    connected: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def set_axis(
        self,
        axis: str,
        value: float,
    ) -> None:
        value = max(-1.0, min(1.0, float(value)))

        if axis == "x":
            self.x = value
        elif axis == "y":
            self.y = value
        elif axis == "z":
            self.z = value
        elif axis == "throttle":
            self.throttle = max(0.0, min(1.0, value))
        else:
            self.metadata.setdefault("axes", {})[axis] = value

    def set_button(
        self,
        button: str,
        pressed: bool,
    ) -> None:
        self.buttons[button] = bool(pressed)


class JoystickManager:
    def __init__(self) -> None:
        self._joysticks: dict[str, JoystickState] = {}

    def register(
        self,
        joystick_id: str,
        name: str,
        metadata: dict[str, Any] | None = None,
    ) -> JoystickState:
        joystick = JoystickState(
            joystick_id=joystick_id,
            name=name,
            connected=True,
            metadata=metadata or {},
        )

        self._joysticks[joystick_id] = joystick

        return joystick

    def get(
        self,
        joystick_id: str,
    ) -> JoystickState | None:
        return self._joysticks.get(joystick_id)

    def list(self) -> list[JoystickState]:
        return list(self._joysticks.values())

    def update_axis(
        self,
        joystick_id: str,
        axis: str,
        value: float,
    ) -> JoystickState:
        joystick = self.get(joystick_id)

        if joystick is None:
            raise KeyError(
                f"Joystick '{joystick_id}' not found"
            )

        joystick.set_axis(axis, value)

        return joystick

    def update_button(
        self,
        joystick_id: str,
        button: str,
        pressed: bool,
    ) -> JoystickState:
        joystick = self.get(joystick_id)

        if joystick is None:
            raise KeyError(
                f"Joystick '{joystick_id}' not found"
            )

        joystick.set_button(button, pressed)

        return joystick

    def disconnect(
        self,
        joystick_id: str,
    ) -> bool:
        joystick = self.get(joystick_id)

        if joystick is None:
            return False

        joystick.connected = False

        return True

    def remove(
        self,
        joystick_id: str,
    ) -> bool:
        return (
            self._joysticks.pop(
                joystick_id,
                None,
            )
            is not None
        )
