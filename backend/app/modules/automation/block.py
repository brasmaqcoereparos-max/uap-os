class AutomationBlock:

    def __init__(
        self,
        block_type,
        name,
        description="",
    ):

        self.block_type = block_type
        self.name = name
        self.description = description

        self.inputs = []
        self.outputs = []
        self.parameters = {}

    def add_input(
        self,
        name,
    ):

        self.inputs.append(name)

    def add_output(
        self,
        name,
    ):

        self.outputs.append(name)

    def set_parameter(
        self,
        name,
        value,
    ):

        self.parameters[name] = value
