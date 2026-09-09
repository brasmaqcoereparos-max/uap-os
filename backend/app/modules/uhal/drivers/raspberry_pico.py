from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class RaspberryPicoDriver(SimulatorDriver):

    BOARD_NAME = (
        "Raspberry Pi Pico"
    )

    MANUFACTURER = (
        "Raspberry Pi"
    )

    GPIO_COUNT = 30

    PWM_PINS = list(
        range(30)
    )

    ADC_CHANNELS = 4

    def __init__(self):

        super().__init__()

        self.board.name = (
            self.BOARD_NAME
        )

        self.board.manufacturer = (
            self.MANUFACTURER
        )

        self.board.capabilities.gpio = (
            self.GPIO_COUNT
        )

        self.board.capabilities.pwm = (
            len(
                self.PWM_PINS
            )
        )

        self.board.capabilities.adc = (
            self.ADC_CHANNELS
        )

        self.board.capabilities.uart = 2

        self.board.capabilities.i2c = 2

        self.board.capabilities.spi = 2

        self.board.capabilities.usb = True
