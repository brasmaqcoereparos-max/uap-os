"""
LED virtual do simulador público UAP.
"""

from app.modules.simulator.devices.virtual_device import (
    VirtualDevice,
)


class VirtualLED(
    VirtualDevice
):

    def __init__(
        self,
        device_id,
        name,
    ):
        super().__init__(
            device_id,
            name,
            "LED",
        )

        self.brightness = 100

    def set_brightness(
        self,
        value,
    ):
        value = int(
            value
        )

        value = max(
            0,
            min(
                100,
                value,
            ),
        )

        self.brightness = value

        if value == 0:
            self.off()

        return self.brightness

    def get_brightness(self):
        return self.brightness

    def reset(self):
        super().reset()

        self.brightness = 100

        return True

    def detailed_status(self):
        data = (
            super().detailed_status()
        )

        data[
            "brightness"
        ] = self.brightness

        return data
