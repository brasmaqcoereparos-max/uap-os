from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ESP32Driver(SimulatorDriver):

    BOARD_NAME = "ESP32"

    GPIO_COUNT = 40
