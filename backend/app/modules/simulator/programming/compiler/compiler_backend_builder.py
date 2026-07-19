from app.modules.simulator.programming.compiler.compiler_backend_writer import (
    compiler_backend_writer,
)


class CompilerBackendBuilder:

    def build(
        self,
        context,
    ):

        compiler_backend_writer.clear()

        compiler_backend_writer.extend(

            context.headers

        )

        compiler_backend_writer.blank()

        compiler_backend_writer.extend(

            context.globals

        )

        compiler_backend_writer.blank()

        compiler_backend_writer.extend(

            context.functions

        )

        compiler_backend_writer.blank()

        compiler_backend_writer.write(

            "void setup() {"

        )

        for line in context.setup:

            compiler_backend_writer.write(

                f"    {line}"

            )

        compiler_backend_writer.write("}")

        compiler_backend_writer.blank()

        compiler_backend_writer.write(

            "void loop() {"

        )

        for line in context.loop:

            compiler_backend_writer.write(

                f"    {line}"

            )

        compiler_backend_writer.write("}")

        return compiler_backend_writer.build()


compiler_backend_builder = CompilerBackendBuilder()
