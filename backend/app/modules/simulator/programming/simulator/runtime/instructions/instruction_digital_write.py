"""
Instrução DIGITAL_WRITE do UAP.

Escreve um estado digital em um pino.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_digital_write(
    pin,
    value,
):
    """
    DIGITAL_WRITE pino, valor
    """

    result = runtime_context.gpio.write(
        int(pin),
        value,
    )

    return result
