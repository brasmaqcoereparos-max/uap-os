from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class TeensyDriver(SimulatorDriver):

    BOARD_NAME = "Teensy"

    GPIO_COUNT = 40

    PWM_PINS = list(range(40))

    ADC_CHANNELS = 18

    DAC_CHANNELS = 2

    HAS_CAN = True
