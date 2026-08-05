from app.modules.automation.devices.outputs.output_base import (
    OutputBase,
)


class Relay(OutputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )
