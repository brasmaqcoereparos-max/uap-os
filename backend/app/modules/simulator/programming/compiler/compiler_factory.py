"""
Fábrica de compiladores do UAP.
"""


class CompilerFactory:

    def __init__(self):
        self._compilers = {}

    def register(
        self,
        name,
        compiler,
    ):
        self._compilers[name] = compiler
        return compiler

    def unregister(
        self,
        name,
    ):
        return self._compilers.pop(
            name,
            None,
        )

    def get(
        self,
        name,
    ):
        return self._compilers.get(name)

    def create(
        self,
        name,
        *args,
        **kwargs,
    ):
        compiler = self.get(name)

        if compiler is None:
            raise KeyError(
                f"Compiler '{name}' not registered"
            )

        if callable(compiler):
            return compiler(
                *args,
                **kwargs,
            )

        return compiler

    def list(self):
        return list(
            self._compilers.keys()
        )


compiler_factory = CompilerFactory()
