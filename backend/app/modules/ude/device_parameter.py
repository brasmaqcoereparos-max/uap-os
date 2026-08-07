class DeviceParameter:

    def __init__(
        self,
        name,
        value=None,
        minimum=None,
        maximum=None,
    ):

        self.name = name

        self.value = value

        self.minimum = minimum

        self.maximum = maximum

    def set(
        self,
        value,
    ):

        if self.minimum is not None:
            if value < self.minimum:
                raise ValueError(
                    "Value below minimum"
                )

        if self.maximum is not None:
            if value > self.maximum:
                raise ValueError(
                    "Value above maximum"
                )

        self.value = value

    def get(self):

        return self.value
