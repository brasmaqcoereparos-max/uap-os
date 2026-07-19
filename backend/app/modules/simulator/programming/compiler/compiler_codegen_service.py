from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)
from app.modules.simulator.programming.compiler.compiler_backend_service import (
    compiler_backend_service,
)

import app.modules.simulator.programming.compiler.backends


class CompilerCodegenService:

    def generate(

        self,

        target,

    ):

        return compiler_backend_service.generate(

            target,

            compiler_ir.all(),

        )


compiler_codegen_service = CompilerCodegenService()
