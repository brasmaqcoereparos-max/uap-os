"""
Instrução CALL do UAP.

Solicita a execução de uma rotina identificada por nome.
"""


class RuntimeCall(Exception):

    def __init__(
        self,
        routine,
        arguments=None,
    ):

        self.routine = str(routine)
        self.arguments = (
            list(arguments)
            if arguments is not None
            else []
        )

        super().__init__(
            f"CALL: {self.routine}"
        )


def instruction_call(
    routine,
    *arguments,
):
    """
    CALL rotina, argumentos...
    """

    if routine is None:
        raise ValueError(
            "O nome da rotina é obrigatório."
        )

    raise RuntimeCall(
        routine,
        arguments,
    )
