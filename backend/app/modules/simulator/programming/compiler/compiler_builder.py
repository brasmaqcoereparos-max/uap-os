from app.modules.simulator.programming.compiler.compiler_preprocessor import (
    compiler_preprocessor,
)
from app.modules.simulator.programming.compiler.compiler_postprocessor import (
    compiler_postprocessor,
)
from app.modules.simulator.programming.compiler.compiler_linker import (
    compiler_linker,
)


class CompilerBuilder:

    def build(
        self,
        sections,
    ):

        processed = []

        for section in sections:

            section = compiler_preprocessor.process(

                section,

            )

            section = compiler_postprocessor.process(

                section,

            )

            processed.append(section)

        return compiler_linker.link(processed)


compiler_builder = CompilerBuilder()
