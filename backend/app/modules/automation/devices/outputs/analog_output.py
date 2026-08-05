from app.modules.automation.devices.outputs.output_base import (
    OutputBase,
)


class AnalogOutput(OutputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.value = 0.0

        self.minimum = 0.0

        self.maximum = 10.0

    def set_value(

        self,

        value,

    ):

        self.value = max(

            self.minimum,

            min(

                self.maximum,

                value,

            ),

        )
