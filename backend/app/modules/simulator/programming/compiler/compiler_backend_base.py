from app.modules.simulator.programming.compiler.compiler_backend import (
    CompilerBackend,
)


class CompilerBackendBase(CompilerBackend):

    def line(
        self,
        text,
        output,
    ):

        output.append(text)

    def blank(
        self,
        output,
    ):

        output.append("")

    def build(
        self,
        output,
    ):

        return "\n".join(output)
