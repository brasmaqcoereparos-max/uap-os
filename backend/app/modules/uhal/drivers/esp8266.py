from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ESP8266Driver(SimulatorDriver):

    BOARD_NAME = "ESP8266"

    MANUFACTURER = "Espressif"

    GPIO_COUNT = 17

    PWM_PINS = list(
        range(17)
    )

    ADC_CHANNELS = 1

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

        self.board.capabilities.wifi = True
