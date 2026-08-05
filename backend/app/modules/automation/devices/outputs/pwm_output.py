from app.modules.automation.devices.outputs.output_base import (
    OutputBase,
)


class PWMOutput(OutputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.duty_cycle = 0

        self.frequency = 1000

    def set_duty_cycle(

        self,

        duty,

    ):

        self.duty_cycle = max(

            0,

            min(

                100,

                duty,

            ),

        )

    def set_frequency(

        self,

        frequency,

    ):

        self.frequency = frequency
