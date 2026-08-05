from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ArduinoUnoDriver(SimulatorDriver):

    def __init__(self):

        super().__init__()

        self.board.name = "Arduino Uno"

        self.board.manufacturer = "Arduino"

        self.board.capabilities.gpio = 20

        self.board.capabilities.pwm = 6

        self.board.capabilities.adc = 6

        self.board.capabilities.uart = 1

        self.board.capabilities.i2c = 1

        self.board.capabilities.spi = 1
