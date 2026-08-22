"""
Instrução PIN_MODE do UAP.

Configura o modo de operação de um pino GPIO.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_pin_mode(
    pin,
    mode,
):
    """
    PIN_MODE pino, modo
    """

    if mode is None:
        raise ValueError(
            "O modo do pino é obrigatório."
        )

    mode = str(mode).upper()

    valid_modes = {
        runtime_context.gpio.INPUT,
        runtime_context.gpio.OUTPUT,
        runtime_context.gpio.INPUT_PULLUP,
    }

    if mode not in valid_modes:
        raise ValueError(
            f"Modo GPIO inválido: {mode}"
        )

    runtime_context.gpio.setup(
        int(pin),
        mode,
    )

    return mode
