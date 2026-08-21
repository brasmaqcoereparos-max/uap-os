"""
Universal Device Engine
Perfis de dispositivos.
"""


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
        )

    def remove_parameter(
        self,
        name,
    ):
        return self.parameters.pop(
            name,
            None,
        )

    def to_dict(self):
        return {
            "name": self.name,
            "device_type": self.device_type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "version": self.version,
            "parameters": dict(
                self.parameters
            ),
        }
