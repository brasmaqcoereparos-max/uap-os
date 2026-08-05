from app.modules.uhal.drivers.esp32 import ESP32Driver


class ESP32C3Driver(ESP32Driver):

    def __init__(self):

        super().__init__()

        self.board.name = "ESP32-C3"

        self.board.capabilities.bluetooth = True

        self.board.capabilities.can = False
