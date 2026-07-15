from app.runtime.driver_base import DriverBase


class SerialDriver(DriverBase):

    def __init__(
        self,
        driver_id: str,
        name: str,
        port: str,
        baudrate: int = 115200,
    ):
        super().__init__(driver_id, name)

        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        try:
            import serial

            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1,
            )

            self.connected = True

        except Exception:
            self.connected = False

    def disconnect(self):
        if self.connection:
            self.connection.close()

        self.connected = False

    def update(self):
        if not self.connected:
            return

        # leitura da serial
        pass
