"""
Construtor da representação intermediária do UAP.
"""

from app.modules.simulator.programming.compiler.compiler_ir import (
    CompilerIR,
    IRInstruction,
)


class IRBuilder:

    def __init__(self):

        self.ir = CompilerIR()

    def emit(
        self,
        opcode,
        *operands,
        metadata=None,
    ):

        return self.ir.emit(
            opcode,
            *operands,
            metadata=metadata,
        )

    def extend(
        self,
        instructions,
    ):

        self.ir.extend(
            instructions
        )

        return self

    def clear(self):

        self.ir.clear()

    def build(self):

        return self.ir.all()

    def instructions(self):

        return list(
            self.ir.instructions
        )

    def __len__(self):

        return len(
            self.ir
        )


compiler_ir_builder = IRBuilder()
