class DeviceIO:

    def __init__(self):

        self.digital_inputs = {}
        self.digital_outputs = {}

        self.analog_inputs = {}
        self.analog_outputs = {}

    def set_digital_input(
        self,
        channel,
        value,
    ):

        self.digital_inputs[channel] = bool(value)

    def read_digital_input(
        self,
        channel,
    ):

        return self.digital_inputs.get(
            channel,
            False,
        )

    def set_digital_output(
        self,
        channel,
        value,
    ):

        self.digital_outputs[channel] = bool(value)

    def read_digital_output(
        self,
        channel,
    ):

        return self.digital_outputs.get(
            channel,
            False,
        )

    def set_analog_input(
        self,
        channel,
        value,
    ):

        self.analog_inputs[channel] = value

    def read_analog_input(
        self,
        channel,
    ):

        return self.analog_inputs.get(
            channel,
            0,
        )

    def set_analog_output(
        self,
        channel,
        value,
    ):

        self.analog_outputs[channel] = value

    def read_analog_output(
        self,
        channel,
    ):

        return self.analog_outputs.get(
            channel,
            0,
  )
