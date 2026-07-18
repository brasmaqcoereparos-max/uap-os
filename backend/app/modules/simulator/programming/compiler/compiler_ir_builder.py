from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)


class CompilerIRBuilder:

    def begin(self):

        compiler_ir.clear()

    def emit(
        self,
        opcode,
        *
