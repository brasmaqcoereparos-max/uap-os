class CompilerFunctions:

    def __init__(self):

        self.functions = {}

    def register(
        self,
        name,
        body,
    ):

        self.functions[name] = body

    def get(
        self,
        name,
    ):

        return self.functions.get(name)

    def exists(
        self,
        name,
    ):

        return name in self.functions

    def all(self):

        return self.functions.copy()

    def clear(self):

        self.functions.clear()


compiler_functions = CompilerFunctions()
