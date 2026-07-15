import socket

from app.runtime.driver_base import DriverBase


class TCPDriver(DriverBase):

    def __init__(
        self,
        driver_id: str,
        name: str,
        host: str,
        port: int,
    ):
        super().__init__(driver_id, name)

        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        try:
            self.socket = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            )

            self.socket.settimeout(3)

            self.socket.connect(
                (
                    self.host,
                    self.port,
                )
            )

            self.connected = True

        except Exception:
            self.connected = False

    def disconnect(self):
        if self.socket:
            self.socket.close()

        self.connected = False

    def update(self):
        if not self.connected:
            return

        pass

    def send(self, data: bytes):
        if self.connected:
            self.socket.sendall(data)

    def receive(self, size: int = 1024):
        if not self.connected:
            return b""

        return self.socket.recv(size)
