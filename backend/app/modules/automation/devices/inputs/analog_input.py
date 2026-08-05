from app.modules.automation.devices.inputs.input_base import (
    InputBase,
)


class AnalogInput(InputBase):

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

    def set_range(

        self,

        minimum,

        maximum,

    ):

        self.minimum = minimum

        self.maximum = maximum
