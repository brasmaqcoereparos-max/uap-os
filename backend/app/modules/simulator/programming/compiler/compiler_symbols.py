class CompilerSymbols:

    def __init__(self):

        self.symbols = {}

    def define(
        self,
        name,
        value,
    ):

        self.symbols[name] = value

    def resolve(
        self,
        name,
        default=None,
    ):

        return self.symbols.get(
            name,
            default,
        )

    def all(self):

        return self.symbols.copy()

    def clear(self):

        self.symbols.clear()


compiler_symbols = CompilerSymbols()
