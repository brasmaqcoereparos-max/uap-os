class CompilerAST:

    def __init__(self):

        self.nodes = []

    def add(

        self,

        node,

    ):

        self.nodes.append(node)

    def remove(

        self,

        node,

    ):

        if node in self.nodes:

            self.nodes.remove(node)

    def all(self):

        return self.nodes.copy()

    def clear(self):

        self.nodes.clear()


compiler_ast = CompilerAST()
