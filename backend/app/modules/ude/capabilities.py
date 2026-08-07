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
            self.communication.append(protocol)

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
        )"""
Universal Device Engine
"""
