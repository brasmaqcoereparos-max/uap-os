from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class BeagleBoneDriver(SimulatorDriver):

    BOARD_NAME = "BeagleBone Black"

    GPIO_COUNT = 65

    PWM_PINS = list(range(65))

    ADC_CHANNELS = 7

    DAC_CHANNELS = 0

    HAS_CAN = True
