"""
Instrução DIGITAL_READ do UAP.

Lê o estado digital de um pino.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_digital_read(
    pin,
):
    """
    DIGITAL_READ pino
    """

    return runtime_context.gpio.read(
        int(pin)
    )
