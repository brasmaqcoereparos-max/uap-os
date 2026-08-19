from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class InputState:
    keys: dict[str, bool] = field(default_factory=dict)
    mouse_x: float = 0.0
    mouse_y: float = 0.0
    mouse_buttons: dict[str, bool] = field(default_factory=dict)
    wheel: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


class InputManager:
    def __init__(self) -> None:
        self.state = InputState()

    def set_key(
        self,
        key: str,
        pressed: bool,
    ) -> None:
        self.state.keys[key] = bool(pressed)

    def is_key_pressed(
        self,
        key: str,
    ) -> bool:
        return self.state.keys.get(
            key,
            False,
        )

    def set_mouse_position(
        self,
        x: float,
        y: float,
    ) -> None:
        self.state.mouse_x = float(x)
        self.state.mouse_y = float(y)

    def set_mouse_button(
        self,
        button: str,
        pressed: bool,
    ) -> None:
        self.state.mouse_buttons[button] = bool(
            pressed
        )

    def set_wheel(
        self,
        value: float,
    ) -> None:
        self.state.wheel = float(value)

    def snapshot(self) -> dict[str, Any]:
        return {
            "keys": dict(self.state.keys),
            "mouse": {
                "x": self.state.mouse_x,
                "y": self.state.mouse_y,
                "buttons": dict(
                    self.state.mouse_buttons
                ),
                "wheel": self.state.wheel,
            },
            "metadata": dict(self.state.metadata),
        }
