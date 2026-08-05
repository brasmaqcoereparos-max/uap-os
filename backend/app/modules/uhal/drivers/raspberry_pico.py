from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class RaspberryPicoDriver(SimulatorDriver):

    BOARD_NAME = "Raspberry Pi Pico"

    GPIO_COUNT = 30

    PWM_PINS = list(range(30))

    ADC_CHANNELS = 4
