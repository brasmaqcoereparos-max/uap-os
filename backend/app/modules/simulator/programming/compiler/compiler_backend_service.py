from app.modules.simulator.programming.compiler.compiler_backend_selector import (
    compiler_backend_selector,
)


class CompilerBackendService:

    def generate(

        self,

        target,

        ir,

    ):

        backend = compiler_backend_selector.select(

            target,

        )

        return backend.generate(ir)


compiler_backend_service = CompilerBackendService()
