"""Representação de uma sequência de movimento."""

class MotionSequence:
    """Sequência composta por vários passos de movimento."""

    def __init__(self, name=None):
        self.name = name or "unnamed"
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def duration(self):
        return sum(getattr(s, 'duration', 0) for s in self.steps)
