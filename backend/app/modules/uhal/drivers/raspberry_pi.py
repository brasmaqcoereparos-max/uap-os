from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class RaspberryPiDriver(SimulatorDriver):

    def __init__(self):

        super().__init__()

        self.board.name = "Raspberry Pi"

        self.board.manufacturer = "Raspberry Pi Foundation"

        self.board.capabilities.gpio = 40

        self.board.capabilities.pwm = 4

        self.board.capabilities.uart = 6

        self.board.capabilities.i2c = 7

        self.board.capabilities.spi = 6

        self.board.capabilities.ethernet = True

        self.board.capabilities.wifi = True

        self.board.capabilities.bluetooth = True
