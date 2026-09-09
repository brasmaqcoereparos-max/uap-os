from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ArduinoNanoDriver(SimulatorDriver):

    BOARD_NAME = (
        "Arduino Nano"
    )

    MANUFACTURER = (
        "Arduino"
    )

    GPIO_COUNT = 22

    PWM_PINS = [
        3,
        5,
        6,
        9,
        10,
        11,
    ]

    ADC_CHANNELS = 8

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

        self.board.capabilities.uart = 1

        self.board.capabilities.i2c = 1

        self.board.capabilities.spi = 1
