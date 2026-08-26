from app.modules.uhal.drivers.raspberry_pi.gpio_controller import (
    gpio_controller,
)

from app.modules.uhal.drivers.raspberry_pi.pin_manager import (
    pin_manager,
)


class GPIODevice:

    def __init__(
        self,
        device_id,
        pin,
        mode="output",
    ):
        self.id = device_id
        self.pin = pin
        self.mode = mode
        self.connected = False

    def connect(self):

        pin_manager.reserve(
            self.pin,
            self.id,
        )

        gpio_controller.initialize()

        if self.mode == "input":
            gpio_controller.setup_input(
                self.pin
            )
        else:
            gpio_controller.setup_output(
                self.pin
            )

        self.connected = True

        return True

    def disconnect(self):

        gpio_controller.cleanup(
            self.pin
        )

        pin_manager.release(
            self.pin
        )

        self.connected = False

        return True

    def read(self):

        if not self.connected:
            self.connect()

        return gpio_controller.read(
            self.pin
        )

    def write(self, value):

        if not self.connected:
            self.connect()

        return gpio_controller.write(
            self.pin,
            value,
        )

    def status(self):

        return {
            "id": self.id,
            "pin": self.pin,
            "mode": self.mode,
            "connected": self.connected,
            "value": gpio_controller.read(
                self.pin
            ),
              }
