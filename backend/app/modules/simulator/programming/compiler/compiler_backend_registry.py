"""
Registro único dos backends de compilação do UAP.
"""


class CompilerBackendRegistry:

    def __init__(self):

        self.backends = {}

    def register(
        self,
        name,
        backend,
    ):

        if not name:
            raise ValueError(
                "Nome do backend é obrigatório."
            )

        self.backends[
            str(name).lower()
        ] = backend

        return backend

    def get(
        self,
        name,
    ):

        if name is None:
            return None

        return self.backends.get(
            str(name).lower()
        )

    def exists(
        self,
        name,
    ):

        return self.get(name) is not None

    def all(self):

        return self.backends.copy()

    def names(self):

        return sorted(
            self.backends.keys()
        )

    def count(self):

        return len(
            self.backends
        )

    def unregister(
        self,
        name,
    ):

        if name is None:
            return None

        return self.backends.pop(
            str(name).lower(),
            None,
        )

    def clear(self):

        self.backends.clear()


compiler_backend_registry = CompilerBackendRegistry()
