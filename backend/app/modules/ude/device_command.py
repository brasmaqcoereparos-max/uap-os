class DeviceCommand:

    def __init__(
        self,
        name,
        action,
        parameters=None,
    ):

        self.name = name

        self.action = action

        self.parameters = parameters or {}

    def set_parameter(
        self,
        name,
        value,
    ):

        self.parameters[name] = value

    def get_parameter(
        self,
        name,
        default=None,
    ):

        return self.parameters.get(
            name,
            default,
        )
