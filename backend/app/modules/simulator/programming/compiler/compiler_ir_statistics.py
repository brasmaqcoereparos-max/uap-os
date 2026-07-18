from collections import Counter

from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)


class CompilerIRStatistics:

    def report(self):

        counter = Counter()

        for instruction in compiler_ir.instructions:

            counter[instruction.opcode] += 1

        return {

            "instructions": len(

                compiler_ir.instructions

            ),

            "opcodes": dict(counter),

        }


compiler_ir_statistics = CompilerIRStatistics()
