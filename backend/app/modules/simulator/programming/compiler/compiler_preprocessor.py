from app.modules.simulator.programming.compiler.compiler_macros import (
    compiler_macros,
)


class CompilerPreprocessor:

    def process(
        self,
        text,
    ):

        for name, value in compiler_macros.all().items():

            text = text.replace(

                f"${name}$",

                str(value),

            )

        return text


compiler_preprocessor = CompilerPreprocessor()
