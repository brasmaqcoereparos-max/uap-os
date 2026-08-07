class DeviceConfiguration:

    def __init__(self):

        self.parameters = {}

    def set(
        self,
        name,
        value,
    ):

        self.parameters[name] = value

    def get(
        self,
        name,
        default=None,
    ):

        return self.parameters.get(
            name,
            default,
        )

    def all(self):

        return dict(
            self.parameters
        )
