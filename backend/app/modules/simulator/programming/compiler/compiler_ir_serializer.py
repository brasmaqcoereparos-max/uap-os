import json

from app.modules.simulator.programming.compiler.compiler_ir import (
    compiler_ir,
)


class CompilerIRSerializer:

    def dumps(self):

        return json.dumps(

            compiler_ir.all(),

            indent=4,

        )

    def loads(self, content):

        return json.loads(content)


compiler_ir_serializer = CompilerIRSerializer()
