class ExecutionContext:

    def __init__(self):

        self.variables = {}

        self.inputs = {}

        self.outputs = {}

    def set_variable(
        self,
        name,
        value,
    ):

        self.variables[name] = value

    def get_variable(
        self,
        name,
        default=None,
    ):

        return self.variables.get(
            name,
            default,
        )

    def clear(self):

        self.variables.clear()

        self.inputs.clear()

        self.outputs.clear()

    def to_dict(self):

        return {

            "variables": self.variables,

            "inputs": self.inputs,

            "outputs": self.outputs,

        }


execution_context = ExecutionContext()
