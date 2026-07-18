from app.modules.simulator.programming.compiler.compiler_writer import (
    compiler_writer,
)


class CompilerGenerator:

    def generate(self, context):

        compiler_writer.clear()

        for include in context["includes"]:

            compiler_writer.write(include)

        compiler_writer.blank()

        for definition in context["definitions"]:

            compiler_writer.write(definition)

        compiler_writer.blank()

        compiler_writer.extend(context["globals"])

        compiler_writer.blank()

        compiler_writer.write("void setup() {")

        for line in context["setup"]:

            compiler_writer.write(f"    {line}")

        compiler_writer.write("}")

        compiler_writer.blank()

        compiler_writer.write("void loop() {")

        for line in context["loop"]:

            compiler_writer.write(f"    {line}")

        compiler_writer.write("}")

        return compiler_writer.build()


compiler_generator = CompilerGenerator()
