from app.modules.automation.devices.inputs.input_base import (
    InputBase,
)


class DigitalInput(InputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.value = False

    def is_active(self):

        return self.value
