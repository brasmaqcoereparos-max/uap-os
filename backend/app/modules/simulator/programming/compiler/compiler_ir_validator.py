from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)


class CompilerIRValidator:

    def validate(self):

        errors = []

        for index, instruction in enumerate(

            compiler_ir.instructions

        ):

            if not instruction.opcode:

                errors.append(

                    {

                        "instruction": index,

                        "error": "Missing opcode",

                    }

                )

        return errors


compiler_ir_validator = CompilerIRValidator()
