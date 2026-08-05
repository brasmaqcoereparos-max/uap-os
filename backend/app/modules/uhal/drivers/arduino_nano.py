from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ArduinoNanoDriver(SimulatorDriver):

    BOARD_NAME = "Arduino Nano"

    GPIO_COUNT = 22

    PWM_PINS = [

        3, 5, 6, 9, 10, 11

    ]

    ADC_CHANNELS = 8
