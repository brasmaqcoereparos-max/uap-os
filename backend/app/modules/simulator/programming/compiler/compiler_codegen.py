from app.modules.simulator.programming.compiler.compiler_source_builder import (
    compiler_source_builder,
)


class CompilerCodeGenerator:

    def generate(
        self,
        context,
    ):

        return compiler_source_builder.build(
            context
        )


compiler_codegen = CompilerCodeGenerator()
