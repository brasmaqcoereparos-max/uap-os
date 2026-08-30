"""
Dispositivo Modbus TCP simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ModbusTCPDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Modbus TCP simulado",
            icon="network",
        )

        self.connected = False

        self.host = None
        self.port = 502
        self.unit_id = 1

        self.registers = {}
        self.coils = {}

        self.last_request = None
        self.request_count = 0

    def connect(
        self,
        host,
        port=502,
        unit_id=1,
    ):
        if not self.enabled:
            return False

        self.host = str(host)
        self.port = int(port)
        self.unit_id = int(unit_id)
        self.connected = True

        return True

    def disconnect(self):
        self.connected = False
        return True

    def write_register(self, address, value):
        if not self.connected:
            return False

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
            return None

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
            return False

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
            return None

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
            "host": self.host,
            "port": self.port,
            "unit_id": self.unit_id,
            "last_request": self.last_request,
        }

    def reset(self):
        self.registers.clear()
        self.coils.clear()

        self.last_request = None
        self.request_count = 0

        self.host = None
        self.port = 502
        self.unit_id = 1

        self.disconnect()
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "connected": self.connected,
            "host": self.host,
            "port": self.port,
            "unit_id": self.unit_id,
            "registers": dict(self.registers),
            "coils": dict(self.coils),
            "last_request": self.last_request,
            "request_count": self.request_count,
        })
        return data
