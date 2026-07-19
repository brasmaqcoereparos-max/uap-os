from app.modules.simulator.programming.compiler.compiler_backend_factory import (
    compiler_backend_factory,
)


class CompilerBackendSelector:

    def select(

        self,

        target,

    ):

        return compiler_backend_factory.create(

            target,

        )


compiler_backend_selector = CompilerBackendSelector()
