from app.modules.automation.devices.outputs.output_base import (
    OutputBase,
)


class DigitalOutput(OutputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.channel = 0

    def set_channel(

        self,

        channel,

    ):

        self.channel = channel
