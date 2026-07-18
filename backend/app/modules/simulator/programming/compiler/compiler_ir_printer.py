from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)


class CompilerIRPrinter:

    def print(self):

        lines = []

        for index, instruction in enumerate(

            compiler_ir.instructions

        ):

            operands = ", ".join(

                map(

                    str,

                    instruction.operands,

                )

            )

            lines.append(

                f"{index:04d}: {instruction.opcode} {operands}"

            )

        return "\n".join(lines)


compiler_ir_printer = CompilerIRPrinter()
