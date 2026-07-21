
from app.modules.simulator.programming.simulator.runtime.runtime_registers import (
    runtime_registers,
)


def instruction_eq(

    register,

    value,

):

    current = runtime_registers.get(

        register,

        None,

    )

    return current == value
