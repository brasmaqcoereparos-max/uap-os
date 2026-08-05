from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)


class ESP32Driver(SimulatorDriver):

    def __init__(self):

        super().__init__()

        self.board.name = "ESP32"

        self.board.manufacturer = "Espressif"

        self.board.capabilities.gpio = 40

        self.board.capabilities.pwm = 16

        self.board.capabilities.adc = 18

        self.board.capabilities.dac = 2

        self.board.capabilities.uart = 3

        self.board.capabilities.i2c = 2

        self.board.capabilities.spi = 4

        self.board.capabilities.can = True

        self.board.capabilities.wifi = True

        self.board.capabilities.bluetooth = True
