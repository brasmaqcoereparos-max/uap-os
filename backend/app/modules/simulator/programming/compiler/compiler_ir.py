class CompilerIR:

    def __init__(self):

        self.instructions = []

    def add(

        self,

        opcode,

        *operands,

    ):

        self.instructions.append(

            {

                "opcode": opcode,

                "operands": list(

                    operands,

                ),

            }

        )

    def all(self):

        return self.instructions.copy()

    def clear(self):

        self.instructions.clear()


compiler_ir = CompilerIR()
