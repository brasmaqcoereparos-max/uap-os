from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)


class CompilerIRBuilder:

    def build(

        self,

        nodes,

    ):

        compiler_ir.clear()

        for node in nodes:

            compiler_ir.add(

                node.get(

                    "block_type",

                    "UNKNOWN",

                ),

                node.get(

                    "id",

                ),

            )

        return compiler_ir.all()


compiler_ir_builder = CompilerIRBuilder()
