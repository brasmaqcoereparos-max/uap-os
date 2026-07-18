class CompilerPassManager:

    def __init__(self):

        self.passes = []

    def register(

        self,

        compiler_pass,

    ):

        self.passes.append(

            compiler_pass,

        )

    def execute(

        self,

        nodes,

    ):

        for compiler_pass in self.passes:

            nodes = compiler_pass.run(

                nodes,

            )

        return nodes

    def clear(self):

        self.passes.clear()


compiler_pass_manager = CompilerPassManager()
