"""
Display OLED simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class OLEDDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="display",
            description="Display OLED",
            icon="display",
        )

        self.lines = []
        self.text = ""

        self.width = 128
        self.height = 64

        self.brightness = 100

    def write(
        self,
        text,
    ):
        if not self.enabled:
            return False

        self.text = str(text)

        return self.text

    def clear(self):
        self.text = ""
        self.lines.clear()

        return True

    def add_line(
        self,
        text,
    ):
        if not self.enabled:
            return False

        value = str(text)

        self.lines.append(value)

        return value

    def set_lines(
        self,
        lines,
    ):
        self.lines = [
            str(item)
            for item in (
                lines or []
            )
        ]

        return list(self.lines)

    def get_text(self):
        return self.text

    def get_lines(self):
        return list(self.lines)

    def set_brightness(
        self,
        brightness,
    ):
        self.brightness = max(
            0,
            min(
                100,
                int(brightness),
            ),
        )

        return self.brightness

    def update(self):
        return {
            "text": self.text,
            "lines": list(
                self.lines
            ),
        }

    def reset(self):
        self.clear()
        self.brightness = 100

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "text": self.text,
            "lines": list(
                self.lines
            ),
            "width": self.width,
            "height": self.height,
            "brightness": (
                self.brightness
            ),
        })

        return data
