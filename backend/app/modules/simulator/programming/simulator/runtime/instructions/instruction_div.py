"""
Instrução DIV do UAP.

Divide o primeiro valor pelo segundo.
"""


def instruction_div(
    a,
    b,
):
    """
    DIV a, b
    """

    if b == 0:
        raise ZeroDivisionError(
            "Não é possível dividir por zero."
        )

    return a / b
