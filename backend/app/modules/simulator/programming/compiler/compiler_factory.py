from app.modules.simulator.programming.compiler.compiler_registry import (
    compiler_registry,
)


class CompilerFactory:

    def register(

        self,

        target,

        compiler,

    ):

        compiler_registry.register(

            target,

            compiler,

        )

    def get(self, target):

        return compiler_registry.get(target)


compiler_factory = CompilerFactory()
