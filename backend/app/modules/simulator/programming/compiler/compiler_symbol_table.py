class CompilerSymbolTable:

    def __init__(self):

        self.table = {}

    def define(

        self,

        name,

        value,

    ):

        self.table[name] = value

    def resolve(

        self,

        name,

    ):

        return self.table.get(name)

    def exists(

        self,

        name,

    ):

        return name in self.table

    def clear(self):

        self.table.clear()

    def all(self):

        return self.table.copy()


compiler_symbol_table = CompilerSymbolTable()
