"""
Seleção do backend de compilação do UAP.
"""

from app.modules.simulator.programming.compiler.compiler_backend_factory import (
    compiler_backend_factory,
)


class CompilerBackendSelector:

    def select(
        self,
        target,
    ):

        return compiler_backend_factory.create(
            target
        )

    def exists(
        self,
        target,
    ):

        return compiler_backend_factory.exists(
            target
        )

    def available(self):

        return compiler_backend_factory.list()


compiler_backend_selector = (
    CompilerBackendSelector()
        )
