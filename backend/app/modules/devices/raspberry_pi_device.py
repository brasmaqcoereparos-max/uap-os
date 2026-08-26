from app.modules.devices.gpio_factory import (
    gpio_factory,
)


class RaspberryPiDevice:

    def __init__(
        self,
        device_id,
        pin,
        mode="output",
    ):
        self.id = device_id
        self.pin = pin
        self.mode = mode
        self.driver_id = "raspberry_pi"
        self.device = None

    def connect(self):

        if self.mode == "input":

            self.device = (
                gpio_factory.create_input(
                    self.id,
                    self.pin,
                )
            )

        else:

            self.device = (
                gpio_factory.create_output(
                    self.id,
                    self.pin,
                )
            )

        return self.device.connect()

    def disconnect(self):

        if self.device is None:
            return True

        result = self.device.disconnect()

        self.device = None

        return result

    def read(self):

        if self.device is None:
            self.connect()

        return self.device.read()

    def write(self, value):

        if self.device is None:
            self.connect()

        return self.device.write(
            value
        )

    def update(self):

        return True

    def status(self):

        if self.device is None:

            return {
                "id": self.id,
                "pin": self.pin,
                "mode": self.mode,
                "connected": False,
            }

        return self.device.status()
