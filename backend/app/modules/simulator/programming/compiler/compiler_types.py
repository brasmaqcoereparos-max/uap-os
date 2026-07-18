class CompilerTypes:

    def __init__(self):

        self.types = {}

    def register(
        self,
        name,
        declaration,
    ):

        self.types[name] = declaration

    def get(
        self,
        name,
    ):

        return self.types.get(name)

    def exists(self, name):

        return name in self.types

    def all(self):

        return self.types.copy()

    def clear(self):

        self.types.clear()


compiler_types = CompilerTypes()
