class DeviceProfile:

    def __init__(
        self,
        name,
        device_type,
    ):

        self.name = name
        self.device_type = device_type

        self.manufacturer = ""
        self.model = ""
        self.version = ""

        self.parameters = {}

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
        )"""
Universal Device Engine
"""
