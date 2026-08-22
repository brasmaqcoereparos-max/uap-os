"""
Gerenciador dos backends de compilação do UAP.
"""

from app.modules.simulator.programming.compiler.compiler_backend_registry import (
    compiler_backend_registry,
)


class CompilerBackendManager:

    def register(self, backend):

        if backend is None:
            raise ValueError(
                "Backend inválido."
            )

        name = getattr(
            backend,
            "name",
            None,
        )

        if not name:
            raise ValueError(
                "O backend precisa possuir um nome."
            )

        compiler_backend_registry.register(
            str(name).lower(),
            backend,
        )

        return backend

    def get(self, target):

        if target is None:
            return None

        return compiler_backend_registry.get(
            str(target).lower()
        )

    def exists(self, target):

        return self.get(target) is not None

    def list(self):

        return sorted(
            compiler_backend_registry.all().keys()
        )

    def generate(
        self,
        target,
        ir,
    ):

        backend = self.get(target)

        if backend is None:
            raise ValueError(
                f"Backend '{target}' não registrado."
            )

        return backend.generate(ir)

    def clear(self):

        compiler_backend_registry.clear()


compiler_backend_manager = CompilerBackendManager()
