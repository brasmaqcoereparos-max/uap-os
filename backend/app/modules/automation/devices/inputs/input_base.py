from app.modules.automation.device import Device


class InputBase(Device):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.value = None

    def read(self):

        return self.value

    def update_value(

        self,

        value,

    ):

        self.value = value
