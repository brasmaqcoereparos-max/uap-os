class FunctionBlock:

    def __init__(
        self,
        block_type,
        name=None,
    ):

        self.block_type = block_type
        self.name = name or block_type
        self.parameters = {}
        self.enabled = True

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

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def to_dict(self):

        return {
            "type": self.block_type,
            "name": self.name,
            "parameters": dict(
                self.parameters
            ),
            "enabled": self.enabled,
        }
