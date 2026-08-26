from app.modules.uhal.drivers.raspberry_pi.gpio_controller import (
    gpio_controller,
)


class GPIOService:

    def initialize(self):
        return gpio_controller.initialize()

    def shutdown(self):
        return gpio_controller.shutdown()

    def output(
        self,
        pin,
        value,
    ):
        gpio_controller.setup_output(pin)
        return gpio_controller.write(
            pin,
            value,
        )

    def input(
        self,
        pin,
    ):
        gpio_controller.setup_input(pin)
        return gpio_controller.read(pin)

    def setup_output(
        self,
        pin,
        initial=False,
    ):
        return gpio_controller.setup_output(
            pin,
            initial,
        )

    def setup_input(
        self,
        pin,
        pull_up=False,
    ):
        return gpio_controller.setup_input(
            pin,
            pull_up,
        )

    def cleanup(
        self,
        pin=None,
    ):
        return gpio_controller.cleanup(
            pin
        )


gpio_service = GPIOService()
