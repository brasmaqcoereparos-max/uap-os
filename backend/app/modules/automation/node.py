class AutomationNode:

    def __init__(
        self,
        node_id,
        node_type,
        name="",
    ):

        self.node_id = node_id
        self.node_type = node_type
        self.name = name

        self.inputs = {}
        self.outputs = {}

        self.parameters = {}

    def set_input(
        self,
        name,
        value,
    ):

        self.inputs[name] = value

    def set_output(
        self,
        name,
        value,
    ):

        self.outputs[name] = value

    def set_parameter(
        self,
        name,
        value,
    ):

        self.parameters[name] = valueu
