class ExecutionPorts:

    def __init__(self):

        self.inputs = {}

        self.outputs = {}

    def set_input(
        self,
        port,
        value,
    ):

        self.inputs[port] = value

    def get_input(
        self,
        port,
        default=0,
    ):

        return self.inputs.get(
            port,
            default,
        )

    def set_output(
        self,
        port,
        value,
    ):

        self.outputs[port] = value

    def get_output(
        self,
        port,
        default=0,
    ):

        return self.outputs.get(
            port,
            default,
        )

    def reset(self):

        self.inputs.clear()
        self.outputs.clear()

    def status(self):

        return {

            "inputs": self.inputs,

            "outputs": self.outputs,

        }


execution_ports = ExecutionPorts()
