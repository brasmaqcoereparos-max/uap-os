from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class BeagleBoneDriver(SimulatorDriver):

    BOARD_NAME = (
        "BeagleBone Black"
    )

    MANUFACTURER = (
        "BeagleBoard.org"
    )

    GPIO_COUNT = 65

    PWM_PINS = list(
        range(65)
    )

    ADC_CHANNELS = 7

    DAC_CHANNELS = 0

    HAS_CAN = True

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

        self.board.capabilities.dac = (
            self.DAC_CHANNELS
        )

        self.board.capabilities.can = (
            self.HAS_CAN
        )

        self.board.capabilities.uart = 5

        self.board.capabilities.i2c = 2

        self.board.capabilities.spi = 2

        self.board.capabilities.ethernet = (
            True
        )
