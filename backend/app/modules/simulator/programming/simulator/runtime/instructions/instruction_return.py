"""
Instrução RETURN do UAP.

Solicita o retorno da rotina atualmente executada.
"""


class RuntimeReturn(Exception):

    def __init__(
        self,
        value=None,
    ):

        self.value = value

        super().__init__(
            "RETURN"
        )


def instruction_return(
    value=None,
):
    """
    RETURN [valor]
    """

    raise RuntimeReturn(
        value
    )
