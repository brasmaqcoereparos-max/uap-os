from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class TeensyDriver(SimulatorDriver):

    BOARD_NAME = "Teensy"

    MANUFACTURER = "PJRC"

    GPIO_COUNT = 40

    PWM_PINS = list(
        range(40)
    )

    ADC_CHANNELS = 18

    DAC_CHANNELS = 2

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

        self.board.capabilities.uart = 8

        self.board.capabilities.i2c = 3

        self.board.capabilities.spi = 3

        self.board.capabilities.usb = True
