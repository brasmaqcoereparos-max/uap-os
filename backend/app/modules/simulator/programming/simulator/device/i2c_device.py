"""
Barramento I2C simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class I2CDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Barramento I2C simulado",
            icon="network",
        )

        self.devices = {}

        self.last_address = None
        self.last_data = None
        self.last_operation = None

        self.frequency = 100000
        self.transaction_count = 0

    def configure(self, frequency=100000):
        frequency = int(frequency)

        if frequency <= 0:
            raise ValueError(
                "A frequência I2C deve ser maior que zero."
            )

        self.frequency = frequency
        return self.frequency

    def register_device(self, address, device):
        address = int(address)

        if not 0 <= address <= 0x7F:
            raise ValueError(
                "Endereço I2C deve estar entre 0x00 e 0x7F."
            )

        self.devices[address] = device
        return device

    def unregister_device(self, address):
        return self.devices.pop(
            int(address),
            None,
        )

    def scan(self):
        return sorted(self.devices.keys())

    def write(self, address, data):
        address = int(address)

        if address not in self.devices:
            return False

        self.last_address = address
        self.last_data = data
        self.last_operation = "write"
        self.transaction_count += 1

        device = self.devices[address]

        writer = getattr(device, "write", None)

        if callable(writer):
            try:
                writer(data)
            except TypeError:
                pass

        return True

    def read(self, address):
        address = int(address)

        self.last_address = address
        self.last_operation = "read"

        device = self.devices.get(address)

        if device is None:
            return None

        self.transaction_count += 1

        reader = getattr(device, "read", None)

        if callable(reader):
            try:
                return reader()
            except TypeError:
                pass

        return device

    def update(self):
        return {
            "devices": self.scan(),
            "frequency": self.frequency,
            "last_address": self.last_address,
            "last_operation": self.last_operation,
        }

    def reset(self):
        self.last_address = None
        self.last_data = None
        self.last_operation = None
        self.transaction_count = 0
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "frequency": self.frequency,
            "addresses": self.scan(),
            "device_count": len(self.devices),
            "last_address": self.last_address,
            "last_data": self.last_data,
            "last_operation": self.last_operation,
            "transaction_count": self.transaction_count,
        })
        return data
