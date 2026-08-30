"""
Dispositivo Modbus RTU simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ModbusRTUDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Modbus RTU simulado",
            icon="network",
        )

        self.connected = False

        self.registers = {}
        self.coils = {}

        self.last_request = None

        self.slave_id = 1
        self.baudrate = 9600

        self.request_count = 0

    def connect(
        self,
        slave_id=1,
        baudrate=9600,
    ):
        self.slave_id = int(slave_id)
        self.baudrate = int(baudrate)

        if self.baudrate <= 0:
            raise ValueError(
                "Baudrate deve ser maior que zero."
            )

        self.connected = True
        return True

    def disconnect(self):
        self.connected = False
        return True

    def write_register(self, address, value):
        if not self.connected:
            self.connect()

        address = int(address)

        self.registers[address] = value

        self.last_request = {
            "operation": "write",
            "address": address,
            "value": value,
        }

        self.request_count += 1
        return True

    def read_register(self, address):
        if not self.connected:
            self.connect()

        address = int(address)

        self.last_request = {
            "operation": "read",
            "address": address,
        }

        self.request_count += 1

        return self.registers.get(
            address,
            0,
        )

    def write_coil(self, address, value):
        if not self.connected:
            self.connect()

        address = int(address)
        self.coils[address] = bool(value)

        self.last_request = {
            "operation": "write_coil",
            "address": address,
            "value": bool(value),
        }

        self.request_count += 1
        return True

    def read_coil(self, address):
        if not self.connected:
            self.connect()

        address = int(address)

        self.last_request = {
            "operation": "read_coil",
            "address": address,
        }

        self.request_count += 1
        return self.coils.get(address, False)

    def update(self):
        return {
            "connected": self.connected,
            "slave_id": self.slave_id,
            "baudrate": self.baudrate,
            "last_request": self.last_request,
        }

    def reset(self):
        self.registers.clear()
        self.coils.clear()
        self.last_request = None
        self.request_count = 0
        self.disconnect()
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "connected": self.connected,
            "slave_id": self.slave_id,
            "baudrate": self.baudrate,
            "registers": dict(self.registers),
            "coils": dict(self.coils),
            "last_request": self.last_request,
            "request_count": self.request_count,
        })
        return data
