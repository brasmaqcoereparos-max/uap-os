"""
Instrução WAIT do UAP.

Permite aguardar um intervalo de tempo.
"""

import time


def instruction_wait(
    milliseconds,
):
    """
    WAIT milissegundos
    """

    milliseconds = max(
        0.0,
        float(milliseconds),
    )

    time.sleep(
        milliseconds / 1000.0,
    )

    return True
