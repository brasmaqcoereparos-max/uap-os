from app.modules.devices.gpio_device import (
    GPIODevice,
)


class DigitalInput(GPIODevice):

    def __init__(
        self,
        device_id,
        pin,
        pull_up=False,
    ):
        super().__init__(
            device_id,
            pin,
            mode="input",
        )

        self.pull_up = bool(
            pull_up
        )

    def connect(self):

        return super().connect()

    def read(self):

        return super().read()

    def is_active(self):

        return bool(
            self.read()
        )

    def is_inactive(self):

        return not self.is_active()

    def status(self):

        data = super().status()

        data["pull_up"] = self.pull_up

        return data
