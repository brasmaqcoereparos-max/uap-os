from app.modules.automation.devices.outputs.output_base import (
    OutputBase,
)


class Solenoid(OutputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.voltage = 24

    def set_voltage(

        self,

        voltage,

    ):

        self.voltage = voltage
