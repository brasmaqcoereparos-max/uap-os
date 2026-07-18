from app.modules.simulator.programming.compiler.compiler_define_manager import (
    compiler_define_manager,
)


class CompilerDefineBuilder:

    def build(self):

        lines = []

        for name, value in compiler_define_manager.all().items():

            if value == "":

                lines.append(

                    f"#define {name}"

                )

            else:

                lines.append(

                    f"#define {name} {value}"

                )

        return lines


compiler_define_builder = CompilerDefineBuilder()
