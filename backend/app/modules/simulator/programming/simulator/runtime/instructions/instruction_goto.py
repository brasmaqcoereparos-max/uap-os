"""
Instrução GOTO do UAP.

Interrompe o fluxo atual e solicita salto para um LABEL.
"""


class RuntimeGoto(Exception):

    def __init__(
        self,
        label,
    ):

        self.label = str(label)

        super().__init__(
            f"GOTO: {self.label}"
        )


def instruction_goto(
    label,
):
    """
    GOTO label
    """

    if label is None:
        raise ValueError(
            "O destino do GOTO é obrigatório."
        )

    raise RuntimeGoto(
        label,
    )
