from app.modules.simulator.programming.simulator.runtime.runtime_registers import (
    runtime_registers,
)


def instruction_gt(

    register,

    value,

):

    current = runtime_registers.get(

        register,

        0,

    )

    return current > value
