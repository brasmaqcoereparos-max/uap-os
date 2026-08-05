from app.modules.automation.devices.outputs.output_base import (
    OutputBase,
)


class SolidStateRelay(OutputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.zero_cross = True
