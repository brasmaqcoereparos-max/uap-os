class AutomationConnection:

    def __init__(
        self,
        source_node,
        source_output,
        target_node,
        target_input,
    ):

        self.source_node = source_node
        self.source_output = source_output

        self.target_node = target_node
        self.target_input = target_input

    def transfer(self):

        value = self.source_node.outputs.get(
            self.source_output
        )

        self.target_node.inputs[
            self.target_input
        ] = value

        return value
