class FunctionBlockParameter:

    def __init__(
        self,
        name,
        value=None,
        parameter_type="generic",
    ):

        self.name = name
        self.value = value
        self.parameter_type = parameter_type

    def set_value(
        self,
        value,
    ):

        self.value = value

    def get_value(self):

        return self.value

    def to_dict(self):

        return {
            "name": self.name,
            "value": self.value,
            "type": self.parameter_type,
        }
