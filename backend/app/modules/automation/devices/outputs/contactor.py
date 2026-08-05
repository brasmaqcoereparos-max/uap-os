from app.modules.automation.devices.outputs.output_base import (
    OutputBase,
)


class Contactor(OutputBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.auxiliary_contacts = 0

    def set_auxiliary_contacts(

        self,

        quantity,

    ):

        self.auxiliary_contacts = quantity
