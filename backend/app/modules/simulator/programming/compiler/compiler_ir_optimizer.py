from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)


class CompilerIROptimizer:

    def optimize(self):

        optimized = []

        previous = None

        for instruction in compiler_ir.instructions:

            if previous is not None:

                if (

                    previous.opcode == instruction.opcode

                    and previous.operands == instruction.operands

                ):

                    continue

            optimized.append(instruction)

            previous = instruction

        compiler_ir.instructions = optimized

        return compiler_ir.all()


compiler_ir_optimizer = CompilerIROptimizer()
