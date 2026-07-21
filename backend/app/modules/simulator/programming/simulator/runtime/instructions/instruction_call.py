from app.modules.simulator.programming.simulator.runtime.runtime_stack import (
    runtime_stack,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_goto import (
    RuntimeGoto,
)


def instruction_call(

    current,

    label,

):

    runtime_stack.push(

        current,

    )

    raise RuntimeGoto(

        label,

    )
