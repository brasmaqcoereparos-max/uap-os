from app.modules.uhal.drivers.esp32 import ESP32Driver


class ESP32S3Driver(ESP32Driver):

    def __init__(self):

        super().__init__()

        self.board.name = "ESP32-S3"

        self.board.capabilities.usb = True

        self.board.capabilities.bluetooth = True
