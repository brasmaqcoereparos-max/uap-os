from app.modules.simulator.programming.compiler.backends.python_backend import (
    PythonBackend,
)


class RaspberryBackend(PythonBackend):

    name = "raspberry"


raspberry_backend = RaspberryBackend()
