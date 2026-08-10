class AutomationPlan:

    def __init__(self):

        self.steps = []

        self.blocks = []

        self.connections = []

        self.explanation = ""

    def add_step(
        self,
        step,
    ):

        self.steps.append(step)

    def add_block(
        self,
        block,
    ):

        self.blocks.append(block)

    def add_connection(
        self,
        connection,
    ):

        self.connections.append(connection)

    def set_explanation(
        self,
        explanation,
    ):

        self.explanation = explanation
