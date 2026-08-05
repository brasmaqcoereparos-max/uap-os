from app.modules.automation.device import Device


class OutputBase(Device):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.state = False

    def on(self):

        self.state = True

    def off(self):

        self.state = False

    def toggle(self):

        self.state = not self.state

    def is_on(self):

        return self.state
