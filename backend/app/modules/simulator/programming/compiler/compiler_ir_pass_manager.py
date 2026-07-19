class CompilerIRPassManager:

    def __init__(self):

        self.passes = []

    def register(
        self,
        compiler_pass,
    ):

        self.passes.append(
            compiler_pass
        )

    def execute(
        self,
        ir,
    ):

        for compiler_pass in self.passes:

            ir = compiler_pass.run(ir)

        return ir

    def clear(self):

        self.passes.clear()

    def all(self):

        return self.passes.copy()


compiler_ir_pass_manager = CompilerIRPassManager()
