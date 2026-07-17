class ExecutionIO:

    def __init__(self):

        self.inputs = {}

        self.outputs = {}

    def input(
        self,
        name,
        value,
    ):

        self.inputs[name] = value

    def output(
        self,
        name,
        value,
    ):

        self.outputs[name] = value

    def read(
        self,
        name,
        default=None,
    ):

        return self.inputs.get(
            name,
            default,
        )

    def write(
        self,
        name,
        default=None,
    ):

        return self.outputs.get(
            name,
            default,
        )

    def clear(self):

        self.inputs.clear()

        self.outputs.clear()

    def status(self):

        return {

            "inputs": self.inputs,

            "outputs": self.outputs,

        }


execution_io = ExecutionIO()
