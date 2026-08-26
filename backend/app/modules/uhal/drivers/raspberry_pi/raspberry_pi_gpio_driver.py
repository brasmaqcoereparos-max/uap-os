from app.modules.uhal.drivers.raspberry_pi.gpio_service import (
    gpio_service,
)


class RaspberryPiGPIODriver:

    def __init__(self):
        self.name = "raspberry_pi_gpio"
        self.initialized = False

    def initialize(self):
        self.initialized = gpio_service.initialize()
        return self.initialized

    def shutdown(self):
        result = gpio_service.shutdown()
        self.initialized = False
        return result

    def connect(self):
        return self.initialize()

    def disconnect(self):
        return self.shutdown()

    def digital_write(
        self,
        pin,
        value,
    ):
        if not self.initialized:
            self.initialize()

        return gpio_service.output(
            pin,
            value,
        )

    def digital_read(
        self,
        pin,
    ):
        if not self.initialized:
            self.initialize()

        return gpio_service.input(
            pin
        )

    def status(self):
        return {
            "name": self.name,
            "initialized": self.initialized,
        }


raspberry_pi_gpio_driver = (
    RaspberryPiGPIODriver()
  )
