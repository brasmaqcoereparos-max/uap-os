"""
Fábrica central de compiladores do UAP.
"""


class CompilerFactory:

    def __init__(self):

        self._compilers = {}

    def register(
        self,
        name,
        compiler,
    ):

        if not name:
            raise ValueError(
                "Nome do compilador é obrigatório."
            )

        if compiler is None:
            raise ValueError(
                "Compilador inválido."
            )

        key = str(
            name
        ).strip().lower()

        self._compilers[key] = compiler

        return compiler

    def unregister(
        self,
        name,
    ):

        if name is None:
            return None

        return self._compilers.pop(
            str(name).strip().lower(),
            None,
        )

    def get(
        self,
        name,
    ):

        if name is None:
            return None

        return self._compilers.get(
            str(name).strip().lower()
        )

    def exists(
        self,
        name,
    ):

        return self.get(name) is not None

    def create(
        self,
        name,
        *args,
        **kwargs,
    ):

        compiler = self.get(name)

        if compiler is None:
            raise KeyError(
                f"Compiler '{name}' não registrado."
            )

        if callable(compiler):

            return compiler(
                *args,
                **kwargs,
            )

        return compiler

    def list(self):

        return sorted(
            self._compilers.keys()
        )

    def clear(self):

        self._compilers.clear()


compiler_factory = CompilerFactory()
