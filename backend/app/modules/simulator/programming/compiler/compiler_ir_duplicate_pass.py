from app.modules.simulator.programming.compiler.compiler_ir_pass import (
    CompilerIRPass,
)


class DuplicateInstructionPass(CompilerIRPass):

    name = "duplicate"

    def run(
        self,
        ir,
    ):

        result = []

        previous = None

        for instruction in ir:

            if instruction == previous:

                continue

            result.append(
                instruction
            )

            previous = instruction

        return result


duplicate_instruction_pass = DuplicateInstructionPass()
