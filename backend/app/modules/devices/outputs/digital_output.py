from app.modules.devices.gpio_device import (
    GPIODevice,
)


class DigitalOutput(GPIODevice):

    def __init__(
        self,
        device_id,
        pin,
        initial=False,
    ):
        super().__init__(
            device_id,
            pin,
            mode="output",
        )

        self.value = bool(initial)

    def connect(self):

        result = super().connect()

        self.write(
            self.value
        )

        return result

    def write(self, value):

        self.value = bool(value)

        return super().write(
            self.value
        )

    def on(self):

        return self.write(True)

    def off(self):

        return self.write(False)

    def toggle(self):

        return self.write(
            not self.value
        )

    def status(self):

        data = super().status()

        data["value"] = self.value

        return data
