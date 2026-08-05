from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ArduinoUnoDriver(SimulatorDriver):

    BOARD_NAME = "Arduino Uno"

    GPIO_COUNT = 20
