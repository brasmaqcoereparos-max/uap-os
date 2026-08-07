"""Gravador de movimentos para registrar e reproduzir."""

class MotionRecorder:
    """Registra comandos/estados durante a execução."""

    def __init__(self):
        self.recorded = []

    def record(self, state):
        self.recorded.append(state)

    def export(self):
        return list(self.recorded)
