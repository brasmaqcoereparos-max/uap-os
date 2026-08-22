"""
Instrução SET do UAP.

Armazena um valor em uma variável do runtime.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_set(
    variable,
    value,
):
    """
    SET variável, valor
    """

    runtime_context.state.set(
        variable,
        value,
    )

    return value
