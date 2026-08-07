"""Algoritmos de interpolação para movimentos."""

def linear_interpolate(a, b, t):
    """Interpolação linear entre a e b por fator t (0..1)."""
    return a + (b - a) * t


# Outros métodos de interpolação podem ser adicionados aqui.
