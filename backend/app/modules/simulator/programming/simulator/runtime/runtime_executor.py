from app.modules.simulator.programming.simulator.runtime.runtime_instruction_set import (
    runtime_instruction_set,
)


class RuntimeExecutor:

    def execute(

        self,

        instruction,

    ):

        callback = runtime_instruction_set.get(

            instruction.opcode,

        )

        if callback is None:

            return False

        callback(

            *instruction.operands,

        )

        return True


runtime_executor = RuntimeExecutor()
