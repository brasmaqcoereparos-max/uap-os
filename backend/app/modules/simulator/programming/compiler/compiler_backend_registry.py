class CompilerBackendRegistry:

    def __init__(self):

        self.backends = {}

    def register(
        self,
        name,
        backend,
    ):

        self.backends[name] = backend

    def get(
        self,
        name,
    ):

        return self.backends.get(name)

    def exists(
        self,
        name,
    ):

        return name in self.backends

    def all(self):

        return self.backends.copy()

    def clear(self):

        self.backends.clear()


compiler_backend_registry = CompilerBackendRegistry()
