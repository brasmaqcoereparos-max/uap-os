from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ArduinoMegaDriver(SimulatorDriver):

    BOARD_NAME = (
        "Arduino Mega"
    )

    MANUFACTURER = (
        "Arduino"
    )

    GPIO_COUNT = 70

    PWM_PINS = [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
    ]

    ADC_CHANNELS = 16

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

        self.board.capabilities.uart = 4

        self.board.capabilities.i2c = 1

        self.board.capabilities.spi = 1
