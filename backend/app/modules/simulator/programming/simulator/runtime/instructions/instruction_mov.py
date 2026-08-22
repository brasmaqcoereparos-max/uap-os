"""
Instrução MOV do UAP.

Move um valor para um registrador do runtime.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_registers import (
    runtime_registers,
)


def instruction_mov(
    register,
    value,
):
    """
    MOV registrador, valor
    """

    runtime_registers.set(
        register,
        value,
    )

    return value
