from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ESP8266Driver(SimulatorDriver):

    BOARD_NAME = "ESP8266"

    GPIO_COUNT = 17

    PWM_PINS = list(range(17))

    ADC_CHANNELS = 1
