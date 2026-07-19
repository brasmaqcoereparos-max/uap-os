from app.modules.simulator.programming.compiler.compiler_ir_pass_manager import (
    compiler_ir_pass_manager,
)
from app.modules.simulator.programming.compiler.compiler_ir_dead_code_pass import (
    dead_code_pass,
)
from app.modules.simulator.programming.compiler.compiler_ir_duplicate_pass import (
    duplicate_instruction_pass,
)


class CompilerIRPipeline:

    def __init__(self):

        compiler_ir_pass_manager.register(
            dead_code_pass
        )

        compiler_ir_pass_manager.register(
            duplicate_instruction_pass
        )

    def optimize(
        self,
        ir,
    ):

        return compiler_ir_pass_manager.execute(
            ir
        )


compiler_ir_pipeline = CompilerIRPipeline()
