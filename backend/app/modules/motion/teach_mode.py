"""Modo de ensino (teach mode) para suscitar movimentos manualmente."""

class TeachMode:
    """Ferramentas auxiliares para ensinar posições/trajectórias."""

    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
