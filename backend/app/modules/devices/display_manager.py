from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Display:
    display_id: str
    name: str
    device_id: str | None = None
    width: int = 800
    height: int = 480
    brightness: int = 100
    message: str = ""
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def set_message(self, message: str) -> None:
        self.message = str(message)

    def set_brightness(self, brightness: int) -> None:
        self.brightness = max(
            0,
            min(100, int(brightness)),
        )


class DisplayManager:
    def __init__(self) -> None:
        self._displays: dict[str, Display] = {}

    def register(
        self,
        display_id: str,
        name: str,
        device_id: str | None = None,
        width: int = 800,
        height: int = 480,
        metadata: dict[str, Any] | None = None,
    ) -> Display:
        display = Display(
            display_id=display_id,
            name=name,
            device_id=device_id,
            width=width,
            height=height,
            metadata=metadata or {},
        )

        self._displays[display_id] = display
        return display

    def get(
        self,
        display_id: str,
    ) -> Display | None:
        return self._displays.get(display_id)

    def list(self) -> list[Display]:
        return list(self._displays.values())

    def message(
        self,
        display_id: str,
        text: str,
    ) -> Display:
        display = self.get(display_id)

        if display is None:
            raise KeyError(
                f"Display '{display_id}' not found"
            )

        display.set_message(text)
        return display

    def brightness(
        self,
        display_id: str,
        value: int,
    ) -> Display:
        display = self.get(display_id)

        if display is None:
            raise KeyError(
                f"Display '{display_id}' not found"
            )

        display.set_brightness(value)
        return display

    def remove(self, display_id: str) -> bool:
        return self._displays.pop(
            display_id,
            None,
        ) is not None
