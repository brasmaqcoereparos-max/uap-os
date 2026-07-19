from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


class RuntimeEngine:

    def initialize(self):

        runtime_context.reset()

    def execute(

        self,

        instructions,

    ):

        for instruction in instructions:

            print(

                instruction,

            )

        return True


runtime_engine = RuntimeEngine()
