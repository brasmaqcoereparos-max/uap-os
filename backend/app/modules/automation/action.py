class AutomationAction:

    def __init__(
        self,
        name,
        action_type,
        parameters=None,
    ):

        self.name = name
        self.action_type = action_type
        self.parameters = parameters or {}

    def set_parameter(
        self,
        name,
        value,
    ):

        self.parameters[name] = value
