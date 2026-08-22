"""
Instrução GET do UAP.

Obtém o valor de uma variável do runtime.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_get(
    variable,
    default=None,
):
    """
    GET variável
    """

    return runtime_context.state.get(
        variable,
        default,
    )
