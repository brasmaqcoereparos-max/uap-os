from app.modules.simulator.programming.compiler.compiler_pipeline import (
    compiler_pipeline,
)
from app.modules.simulator.programming.compiler.compiler_executor import (
    compiler_executor,
)
from app.modules.simulator.programming.compiler.compiler_generator import (
    compiler_generator,
)


class CompilerProgram:

    def compile(

        self,

        canvas,

        context,

    ):

        nodes = compiler_pipeline.process(

            canvas,

        )

        compiler_executor.execute(

            nodes,

            context,

        )

        return compiler_generator.generate(

            context.build()

        )


compiler_program = CompilerProgram()
