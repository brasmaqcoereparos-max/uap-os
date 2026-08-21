"""
Dispositivo Modbus TCP simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ModbusTCPDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.host = None
        self.port = 502
        self.registers = {}
        self.last_request = None

    def connect(
        self,
        host,
        port=502,
    ):

        self.host = host
        self.port = port
        self.connected = True

    def disconnect(self):

        self.connected = False

    def write_register(
        self,
        address,
        value,
    ):

        if not self.connected:
            return False

        self.registers[address] = value

        self.last_request = {
            "operation": "write",
            "address": address,
            "value": value,
        }

        return True

    def read_register(
        self,
        address,
    ):

        if not self.connected:
            return None

        self.last_request = {
            "operation": "read",
            "address": address,
        }

        return self.registers.get(
            address,
            0,
        )

    def update(self):
        pass

    def reset(self):

        self.registers.clear()
        self.last_request = None
        self.disconnect()
