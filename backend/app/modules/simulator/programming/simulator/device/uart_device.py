"""
UART simulada do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class UARTDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="UART simulada",
            icon="network",
        )

        self.connected = False

        self.baudrate = 9600
        self.data_bits = 8
        self.stop_bits = 1
        self.parity = "none"

        self.buffer = []
        self.tx_buffer = []
        self.rx_buffer = []

        self.bytes_sent = 0
        self.bytes_received = 0

    def connect(
        self,
        baudrate=9600,
        data_bits=8,
        stop_bits=1,
        parity="none",
    ):
        baudrate = int(baudrate)

        if baudrate <= 0:
            raise ValueError(
                "Baudrate deve ser maior que zero."
            )

        self.baudrate = baudrate
        self.data_bits = int(data_bits)
        self.stop_bits = int(stop_bits)
        self.parity = str(parity).lower()

        self.connected = True
        return True

    def disconnect(self):
        self.connected = False
        return True

    def write(self, data):
        if not self.connected:
            return False

        self.buffer.append(data)
        self.tx_buffer.append(data)

        self.bytes_sent += len(
            str(data).encode("utf-8")
        )

        return True

    def read(self):
        if self.rx_buffer:
            data = self.rx_buffer.pop(0)

            self.bytes_received += len(
                str(data).encode("utf-8")
            )

            return data

        if self.buffer:
            return self.buffer.pop(0)

        return None

    def inject_received(self, data):
        self.rx_buffer.append(data)
        return True

    def available(self):
        return (
            len(self.rx_buffer)
            + len(self.buffer)
        )

    def update(self):
        return {
            "connected": self.connected,
            "baudrate": self.baudrate,
            "available": self.available(),
        }

    def reset(self):
        self.buffer.clear()
        self.tx_buffer.clear()
        self.rx_buffer.clear()

        self.bytes_sent = 0
        self.bytes_received = 0

        self.disconnect()
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "connected": self.connected,
            "baudrate": self.baudrate,
            "data_bits": self.data_bits,
            "stop_bits": self.stop_bits,
            "parity": self.parity,
            "available": self.available(),
            "bytes_sent": self.bytes_sent,
            "bytes_received": self.bytes_received,
        })
        return data
