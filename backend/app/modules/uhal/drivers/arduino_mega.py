from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ArduinoMegaDriver(SimulatorDriver):

    BOARD_NAME = "Arduino Mega"

    GPIO_COUNT = 70

    PWM_PINS = [

        2, 3, 4, 5, 6, 7,

        8, 9, 10, 11, 12, 13

    ]

    ADC_CHANNELS = 16
