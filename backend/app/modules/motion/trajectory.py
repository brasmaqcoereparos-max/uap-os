"""Representação de trajetórias."""

class Trajectory:
    """Armazena uma sequência contínua de poses ou pontos."""

    def __init__(self, points=None):
        self.points = points or []

    def length(self):
        return len(self.points)
