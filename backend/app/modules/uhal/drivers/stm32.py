from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class STM32Driver(SimulatorDriver):

    BOARD_NAME = "STM32"

    MANUFACTURER = (
        "STMicroelectronics"
    )

    GPIO_COUNT = 80

    PWM_PINS = list(
        range(80)
    )

    ADC_CHANNELS = 24

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

        self.board.capabilities.uart = 6

        self.board.capabilities.i2c = 3

        self.board.capabilities.spi = 3

        self.board.capabilities.can = True

        self.board.capabilities.usb = True
