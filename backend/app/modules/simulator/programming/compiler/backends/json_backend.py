import json

from app.modules.simulator.programming.compiler.compiler_backend_base import (
    CompilerBackendBase,
)


class JsonBackend(CompilerBackendBase):

    name = "json"

    def generate(
        self,
        ir,
    ):

        return json.dumps(

            ir,

            indent=4,

        )


json_backend = JsonBackend()
