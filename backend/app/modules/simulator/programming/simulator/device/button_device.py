"""
Botão digital simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


class ButtonDevice(DeviceBase):
    def __init__(
        self,
        name,
        pin,
    ):
        super().__init__(
            name=name,
            category="input",
            description="Botão digital",
            icon="button",
        )

        self.pin = pin
        self.pressed = False

    def press(self):
        if not self.enabled:
            return False

        self.pressed = True

        runtime_gpio.write(
            self.pin,
            True,
        )

        return True

    def release(self):
        self.pressed = False

        runtime_gpio.write(
            self.pin,
            False,
        )

        return True

    def read(self):
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
                self.pressed = bool(
                    value
                )

        return self.pressed

    def update(self):
        return self.read()

    def reset(self):
        return self.release()

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "pin": self.pin,
            "pressed": self.pressed,
        })

        return data
