from app.modules.simulator.programming.simulator.runtime.runtime_instruction_set import (
    runtime_instruction_set,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_mov import (
    instruction_mov,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_set import (
    instruction_set,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_get import (
    instruction_get,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_wait import (
    instruction_wait,
)


class RuntimeInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:

            return

        runtime_instruction_set.register(

            "MOV",

            instruction_mov,

        )

        runtime_instruction_set.register(

            "SET",

            instruction_set,

        )

        runtime_instruction_set.register(

            "GET",

            instruction_get,

        )

        runtime_instruction_set.register(

            "WAIT",

            instruction_wait,

        )

        cls.initialized = True
