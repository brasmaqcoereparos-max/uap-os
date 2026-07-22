from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_adc import (
    runtime_adc,
)


class PotentiometerDevice(DeviceBase):

    def __init__(

        self,

        name,

        pin,

    ):

        super().__init__(name)

        self.pin = pin

        self.value = 0

    def set_value(

        self,

        value,

    ):

        value = max(

            0,

            min(

                4095,

                int(value),

            ),

        )

        self.value = value

        runtime_adc.set(

            self.pin,

            value,

        )

    def update(self):

        pass

    def reset(self):

        self.set_value(0)
