class AutomationTrigger:

    def __init__(
        self,
        name,
        trigger_type,
        parameters=None,
    ):

        self.name = name
        self.trigger_type = trigger_type
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
