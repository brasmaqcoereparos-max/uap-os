from app.modules.automation.devices.inputs.digital_input import (
    DigitalInput,
)


class Button(DigitalInput):

    def press(self):

        self.value = True

    def release(self):

        self.value = False
