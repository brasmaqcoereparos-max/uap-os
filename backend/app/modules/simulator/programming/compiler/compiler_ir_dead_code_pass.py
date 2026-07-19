from app.modules.simulator.programming.compiler.compiler_ir_pass import (
    CompilerIRPass,
)


class DeadCodePass(CompilerIRPass):

    name = "dead_code"

    def run(
        self,
        ir,
    ):

        optimized = []

        for instruction in ir:

            if instruction.get("opcode") == "NOP":

                continue

            optimized.append(
                instruction
            )

        return optimized


dead_code_pass = DeadCodePass()
