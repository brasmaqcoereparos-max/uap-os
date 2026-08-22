"""
Instrução LABEL do UAP.

Cria um marcador para controle de fluxo.
"""


def instruction_label(
    name,
):
    """
    LABEL nome
    """

    if name is None:
        raise ValueError(
            "O nome do LABEL é obrigatório."
        )

    return str(name)
