"""
Fábrica central dos backends de compilação do UAP.
"""

from app.modules.simulator.programming.compiler.backends.backend_initializer import (
    BackendInitializer,
)

from app.modules.simulator.programming.compiler.compiler_backend_registry import (
    compiler_backend_registry,
)


class CompilerBackendFactory:

    def __init__(self):
        self.initialized = False

    def initialize(self):
        if self.initialized:
            return

        BackendInitializer.initialize()
        self.initialized = True

    def create(self, target):

        self.initialize()

        if target is None:
            raise ValueError(
                "O alvo do compilador é obrigatório."
            )

        target = str(target).strip().lower()

        backend = compiler_backend_registry.get(
            target
        )

        if backend is None:
            raise ValueError(
                f"Backend '{target}' não registrado."
            )

        return backend

    def exists(self, target):

        self.initialize()

        if target is None:
            return False

        return compiler_backend_registry.exists(
            str(target).strip().lower()
        )

    def list(self):

        self.initialize()

        return sorted(
            compiler_backend_registry.all().keys()
        )


compiler_backend_factory = CompilerBackendFactory()
