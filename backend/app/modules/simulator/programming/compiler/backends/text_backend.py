from app.modules.simulator.programming.compiler.compiler_backend_base import (
    CompilerBackendBase,
)


class TextBackend(CompilerBackendBase):

    name = "text"

    def generate(
        self,
        ir,
    ):

        output = []

        for instruction in ir:

            output.append(

                str(instruction)

            )

        return "\n".join(output)


text_backend = TextBackend()
