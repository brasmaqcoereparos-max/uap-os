
class CompilerMacros:

    def __init__(self):

        self.macros = {}

    def define(
        self,
        name,
        value,
    ):

        self.macros[name] = value

    def get(
        self,
        name,
    ):

        return self.macros.get(name)

    def exists(
        self,
        name,
    ):

        return name in self.macros

    def all(self):

        return self.macros.copy()

    def clear(self):

        self.macros.clear()


compiler_macros = CompilerMacros()
