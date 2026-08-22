"""
Instrução ANALOG_READ do UAP.

Lê um valor analógico do dispositivo GPIO/runtime.

No simulador, quando não existir uma entrada analógica física,
o valor previamente definido no canal é retornado.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_analog_read(
    pin,
):
    """
    ANALOG_READ pino
    """

    pin = int(pin)

    analog = getattr(
        runtime_context,
        "analog",
        None,
    )

    if analog is not None:

        reader = getattr(
            analog,
            "read",
            None,
        )

        if callable(reader):
            return reader(pin)

    return 0
