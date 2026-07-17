class ExecutionVariables:

    def __init__(self):

        self.variables = {}

    def set(
        self,
        name,
        value,
    ):

        self.variables[name] = value

    def get(
        self,
        name,
        default=None,
    ):

        return self.variables.get(
            name,
            default,
        )

    def exists(
        self,
        name,
    ):

        return name in self.variables

    def remove(
        self,
        name,
    ):

        self.variables.pop(
            name,
            None,
        )

    def clear(self):

        self.variables.clear()

    def all(self):

        return self.variables.copy()


execution_variables = ExecutionVariables()
