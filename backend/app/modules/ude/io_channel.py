from enum import Enum


class IOType(Enum):

    DIGITAL_INPUT = "digital_input"

    DIGITAL_OUTPUT = "digital_output"

    ANALOG_INPUT = "analog_input"

    ANALOG_OUTPUT = "analog_output"

    PWM = "pwm"


class IOChannel:

    def __init__(
        self,
        channel,
        io_type,
    ):

        self.channel = channel
        self.io_type = io_type
        self.value = 0
        self.enabled = True

    def write(
        self,
        value,
    ):

        self.value = value

    def read(self):

        return self.value
