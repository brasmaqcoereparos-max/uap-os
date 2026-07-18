from app.modules.simulator.programming.compiler.compiler_include_builder import (
    compiler_include_builder,
)
from app.modules.simulator.programming.compiler.compiler_define_builder import (
    compiler_define_builder,
)
from app.modules.simulator.programming.compiler.compiler_global_builder import (
    compiler_global_builder,
)
from app.modules.simulator.programming.compiler.compiler_setup_builder import (
    compiler_setup_builder,
)
from app.modules.simulator.programming.compiler.compiler_loop_builder import (
    compiler_loop_builder,
)
from app.modules.simulator.programming.compiler.compiler_builder import (
    compiler_builder,
)


class CompilerSourceBuilder:

    def build(
        self,
        context,
    ):

        sections = [

            "\n".join(

                compiler_include_builder.build()

            ),

            "\n".join(

                compiler_define_builder.build()

            ),

            "\n".join(

                compiler_global_builder.build(

                    context.globals

                )

            ),

            "\n".join(

                compiler_setup_builder.build(

                    context.setup

                )

            ),

            "\n".join(

                compiler_loop_builder.build(

                    context.loop

                )

            ),

        ]

        return compiler_builder.build(

            sections

        )


compiler_source_builder = CompilerSourceBuilder()
