"""
Serviço de geração de código através dos backends do UAP.
"""

from app.modules.simulator.programming.compiler.compiler_backend_factory import (
    compiler_backend_factory,
)


class CompilerBackendService:

    def generate(
        self,
        target,
        ir,
    ):
        if target is None:
            raise ValueError(
                "O target do compilador é obrigatório."
            )

        if ir is None:
            raise ValueError(
                "A representação intermediária é obrigatória."
            )

        backend = compiler_backend_factory.create(
            target
        )

        generator = getattr(
            backend,
            "generate",
            None,
        )

        if not callable(generator):
            raise TypeError(
                f"O backend '{target}' não possui "
                "o método generate()."
            )

        return generator(ir)

    def available(self):

        return compiler_backend_factory.list()

    def exists(
        self,
        target,
    ):

        return compiler_backend_factory.exists(
            target
        )


compiler_backend_service = CompilerBackendService()
