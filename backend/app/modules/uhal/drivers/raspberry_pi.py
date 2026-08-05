from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class RaspberryPiDriver(SimulatorDriver):

    BOARD_NAME = "Raspberry Pi"

    GPIO_COUNT = 40
