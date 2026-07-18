class IRInstruction:

    def __init__(
        self,
        opcode,
        *operands,
    ):

        self.opcode = opcode

        self.operands = list(operands)

    def to_dict(self):

        return {

            "opcode": self.opcode,

            "operands": self.operands,

        }


class CompilerIR:

    def __init__(self):

        self.instructions = []

    def emit(
        self,
        opcode,
        *operands,
    ):

        self.instructions.append(

            IRInstruction(

                opcode,

                *operands,

            )

        )

    def all(self):

        return [

            item.to_dict()

            for item

            in self.instructions

        ]

    def clear(self):

        self.instructions.clear()


compiler_ir = CompilerIR()
