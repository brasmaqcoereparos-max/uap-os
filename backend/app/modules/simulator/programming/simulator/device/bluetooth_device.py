"""
Dispositivo Bluetooth simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class BluetoothDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Comunicação Bluetooth simulada",
            icon="bluetooth",
        )

        self.connected = False
        self.device = None
        self.paired_devices = []
        self.tx_buffer = []
        self.rx_buffer = []
        self.bytes_sent = 0
        self.bytes_received = 0

    def connect(self, device):
        if not self.enabled:
            return False

        self.device = str(device)
        self.connected = True

        if self.device not in self.paired_devices:
            self.paired_devices.append(self.device)

        return True

    def disconnect(self):
        self.connected = False
        self.device = None
        return True

    def send(self, data):
        if not self.enabled or not self.connected:
            return False

        self.tx_buffer.append(data)
        self.bytes_sent += len(str(data).encode("utf-8"))
        return True

    def receive(self):
        if not self.rx_buffer:
            return None

        data = self.rx_buffer.pop(0)
        self.bytes_received += len(str(data).encode("utf-8"))
        return data

    def inject_received(self, data):
        self.rx_buffer.append(data)
        return True

    def is_connected(self):
        return self.connected

    def update(self):
        return {
            "connected": self.connected,
            "device": self.device,
            "tx_pending": len(self.tx_buffer),
            "rx_pending": len(self.rx_buffer),
        }

    def reset(self):
        self.disconnect()
        self.tx_buffer.clear()
        self.rx_buffer.clear()
        self.bytes_sent = 0
        self.bytes_received = 0
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "connected": self.connected,
            "device": self.device,
            "paired_devices": list(self.paired_devices),
            "tx_pending": len(self.tx_buffer),
            "rx_pending": len(self.rx_buffer),
            "bytes_sent": self.bytes_sent,
            "bytes_received": self.bytes_received,
        })
        return data
