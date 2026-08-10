from enum import Enum


class ParameterType(Enum):

    NUMBER = "number"

    TEXT = "text"

    BOOLEAN = "boolean"

    SELECT = "select"

    TIME = "time"

    DEVICE = "device"

    SENSOR = "sensor"


class BlockParameter:

    def __init__(
        self,
        name,
        parameter_type,
        default=None,
        description="",
    ):

        self.name = name
        self.parameter_type = parameter_type
        self.default = default
        self.value = default
        self.description = description

    def set(self, value):

        self.value = value

    def get(self):

        return self.value
