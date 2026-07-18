from app.modules.simulator.programming.compiler.compiler_include_manager import (
    compiler_include_manager,
)


class CompilerIncludeBuilder:

    def build(self):

        return [

            f"#include {include}"

            for include

            in compiler_include_manager.all()

        ]


compiler_include_builder = CompilerIncludeBuilder()
