"""
Relé virtual do simulador público UAP.
"""

from app.modules.simulator.devices.virtual_device import (
    VirtualDevice,
)


class VirtualRelay(
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
            "RELAY",
        )

        self.switch_count = 0

    def on(self):
        previous = self.state

        result = super().on()

        if (
            result
            and not previous
        ):
            self.switch_count += 1

        return result

    def off(self):
        previous = self.state

        result = super().off()

        if previous:
            self.switch_count += 1

        return result

    def toggle(self):
        if not self.enabled:
            return self.state

        result = super().toggle()

        self.switch_count += 1

        return result

    def reset(self):
        super().reset()

        self.switch_count = 0

        return True

    def detailed_status(self):
        data = (
            super().detailed_status()
        )

        data[
            "switch_count"
        ] = self.switch_count

        return data
