from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class ModbusRTUDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.registers = {}

    def write_register(
        self,
        address,
        value,
    ):
        self.registers[address] = value

    def read_register(
        self,
        address,
    ):
        return self.registers.get(address, 0)

    def update(self):
        pass

    def reset(self):
        self.registers.clear()
