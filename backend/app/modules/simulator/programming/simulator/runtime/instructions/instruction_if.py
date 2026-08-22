"""
Instrução IF do UAP.

Executa um salto quando a condição for verdadeira.
"""

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_goto import (
    RuntimeGoto,
)


def instruction_if(
    condition,
    label,
):
    """
    IF condição, LABEL
    """

    if bool(condition):

        if label is None:
            raise ValueError(
                "O destino do IF é obrigatório."
            )

        raise RuntimeGoto(
            label,
        )

    return False
