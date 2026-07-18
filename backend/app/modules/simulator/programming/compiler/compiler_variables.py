class CompilerVariables:

    def __init__(self):

        self.variables = {}

    def add(
        self,
        name,
        value=None,
    ):

        self.variables[name] = value

    def exists(self, name):

        return name in self.variables

    def get(
        self,
        name,
        default=None,
    ):

        return self.variables.get(
            name,
            default,
        )

    def all(self):

        return self.variables.copy()

    def clear(self):

        self.variables.clear()


compiler_variables = CompilerVariables()
