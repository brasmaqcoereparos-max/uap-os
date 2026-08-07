"""Biblioteca de movimentos reutilizáveis."""

_motion_library = {}

def register_motion(name, sequence):
    _motion_library[name] = sequence


def get_motion(name):
    return _motion_library.get(name)
