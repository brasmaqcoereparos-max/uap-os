"""
Botão virtual do simulador público UAP.
"""

from app.modules.simulator.devices.virtual_device import (
    VirtualDevice,
)


class VirtualButton(
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
            "BUTTON",
        )

        self.press_count = 0

    def press(self):
        if not self.enabled:
            return False

        self.state = True
        self.press_count += 1

        self._touch()

        return True

    def release(self):
        if not self.state:
            return False

        self.state = False

        self._touch()

        return True

    def is_pressed(self):
        return bool(
            self.state
        )

    def reset(self):
        super().reset()

        self.press_count = 0

        return True

    def detailed_status(self):
        data = (
            super().detailed_status()
        )

        data[
            "press_count"
        ] = self.press_count

        return data
