from app.modules.simulator.programming.compiler.compiler_backend_registry import (
    compiler_backend_registry,
)


class CompilerBackendManager:

    def register(
        self,
        backend,
    ):

        compiler_backend_registry.register(

            backend.name,

            backend,

        )

    def generate(
        self,
        target,
        ir,
    ):

        backend = compiler_backend_registry.get(
            target
        )

        if backend is None:

            raise ValueError(

                f"Backend '{target}' not registered."

            )

        return backend.generate(ir)


compiler_backend_manager = CompilerBackendManager()
