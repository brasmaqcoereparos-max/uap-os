"""
Universal Device Engine
Capacidades dos dispositivos.
"""


class DeviceCapabilities:

    def __init__(self):
        self.inputs = 0
        self.outputs = 0

        self.analog_inputs = 0
        self.analog_outputs = 0

        self.pwm = False
        self.encoder = False

        self.communication = []

        self.motion = False
        self.sensing = False
        self.vision = False

    def add_communication(
        self,
        protocol,
    ):
        if protocol not in self.communication:
            self.communication.append(
                protocol
            )

    def remove_communication(
        self,
        protocol,
    ):
        if protocol in self.communication:
            self.communication.remove(
                protocol
            )
            return True

        return False

    def supports(
        self,
        feature,
    ):
        return bool(
            getattr(
                self,
                feature,
                False,
            )
        )

    def to_dict(self):
        return {
            "inputs": self.inputs,
            "outputs": self.outputs,
            "analog_inputs": self.analog_inputs,
            "analog_outputs": self.analog_outputs,
            "pwm": self.pwm,
            "encoder": self.encoder,
            "communication": list(
                self.communication
            ),
            "motion": self.motion,
            "sensing": self.sensing,
            "vision": self.vision,
        }
