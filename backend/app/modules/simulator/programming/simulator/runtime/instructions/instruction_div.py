
from app.modules.simulator.programming.simulator.runtime.runtime_registers import (
    runtime_registers,
)


def instruction_div(

    register,

    value,

):

    if value == 0:

        return

    current = runtime_registers.get(

        register,

        0,

    )

    runtime_registers.set(

        register,

        current / value,

    )
