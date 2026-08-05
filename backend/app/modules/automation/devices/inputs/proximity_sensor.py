from app.modules.automation.devices.inputs.digital_input import (
    DigitalInput,
)


class ProximitySensor(DigitalInput):

    def detect(self):

        self.value = True

    def clear(self):

        self.value = False
