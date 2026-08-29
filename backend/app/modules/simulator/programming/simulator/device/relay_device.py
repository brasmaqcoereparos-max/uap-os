"""
Relé simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


class RelayDevice(DeviceBase):
    def __init__(
        self,
        name,
        pin,
    ):
        super().__init__(
            name=name,
            category="output",
            description="Relé digital",
            icon="relay",
        )

        self.pin = pin
        self.state = False

    def on(self):
        if not self.enabled:
            return False

        self.state = True

        runtime_gpio.write(
            self.pin,
            True,
        )

        return True

    def off(self):
        self.state = False

        runtime_gpio.write(
            self.pin,
            False,
        )

        return True

    def toggle(self):
        if self.state:
            return self.off()

        return self.on()

    def update(self):
        reader = getattr(
            runtime_gpio,
            "read",
            None,
        )

        if callable(reader):
            value = reader(
                self.pin
            )

            if value is not None:
                self.state = bool(
                    value
                )

        return self.state

    def reset(self):
        return self.off()

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "pin": self.pin,
            "state": self.state,
        })

        return data
