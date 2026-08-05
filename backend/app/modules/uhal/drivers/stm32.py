from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class STM32Driver(SimulatorDriver):

    BOARD_NAME = "STM32"

    GPIO_COUNT = 80

    PWM_PINS = list(range(80))

    ADC_CHANNELS = 24
