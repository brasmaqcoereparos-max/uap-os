from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class TemperatureSensorDevice(DeviceBase):

    def __init__(

        self,

        name,

    ):

        super().__init__(name)

        self.temperature = 25.0

    def set_temperature(

        self,

        value,

    ):

        self.temperature = float(value)

    def read(self):

        return self.temperature

    def update(self):

        pass

    def reset(self):

        self.temperature = 25.0
