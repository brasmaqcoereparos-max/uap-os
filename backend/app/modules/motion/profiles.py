"""Perfis de movimento (velocidade/ aceleração etc.)."""

class Profile:
    """Perfil genérico de velocidade/ aceleração."""

    def __init__(self, name=None, max_speed=None, max_accel=None):
        self.name = name
        self.max_speed = max_speed
        self.max_accel = max_accel
