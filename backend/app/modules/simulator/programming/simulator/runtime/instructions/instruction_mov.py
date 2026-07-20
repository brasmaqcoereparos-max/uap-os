from app.modules.simulator.programming.simulator.runtime.runtime_registers import (
    runtime_registers,
)


def instruction_mov(

    register,

    value,

):

    runtime_registers.set(

        register,

        value,

    )
