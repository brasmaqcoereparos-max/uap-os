from app.modules.simulator.programming.compiler.compiler_result import (
    CompilerResult,
)
from app.modules.simulator.programming.compiler.compiler_validator import (
    compiler_validator,
)


class CompilerEngine:

    def compile(

        self,

        compiler,

        canvas,

    ):

        result = CompilerResult()

        errors = compiler_validator.validate(

            canvas

        )

        if errors:

            for error in errors:

                result.add_error(error)

            return result

        compiler.reset()

        compiler.compile(canvas)

        result.set_output(

            compiler.context().build()

        )

        return result


compiler_engine = CompilerEngine()
