class CompilerConstants:

    def __init__(self):

        self.constants = {}

    def add(
        self,
        name,
        value,
    ):

        self.constants[name] = value

    def get(
        self,
        name,
    ):

        return self.constants.get(name)

    def exists(self, name):

        return name in self.constants

    def all(self):

        return self.constants.copy()

    def clear(self):

        self.constants.clear()


compiler_constants = CompilerConstants()
