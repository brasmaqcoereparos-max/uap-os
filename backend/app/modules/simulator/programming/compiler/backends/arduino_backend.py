from app.modules.simulator.programming.compiler.compiler_backend_base import (
    CompilerBackendBase,
)
from app.modules.simulator.programming.compiler.compiler_backend_builder import (
    compiler_backend_builder,
)
from app.modules.simulator.programming.compiler.compiler_backend_context import (
    CompilerBackendContext,
)


class ArduinoBackend(CompilerBackendBase):

    name = "arduino"

    def generate(
        self,
        ir,
    ):

        context = CompilerBackendContext()

        context.add_header("#include <Arduino.h>")

        context.add_setup("Serial.begin(115200);")

        for instruction in ir:

            opcode = instruction.get("opcode")

            context.add_loop(

                f"// {opcode}"

            )

        return compiler_backend_builder.build(

            context

        )


arduino_backend = ArduinoBackend()
