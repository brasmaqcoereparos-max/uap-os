from app.modules.automation.devices.inputs.digital_input import (
    DigitalInput,
)


class LimitSwitch(DigitalInput):

    def trigger(self):

        self.value = True

    def reset(self):

        self.value = False
