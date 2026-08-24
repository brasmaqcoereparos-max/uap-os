"""
Contexto compartilhado durante a compilação UAP.
"""


class CompilerContext:

    def __init__(self):

        self.reset()

    def reset(self):

        self.variables = {}
        self.includes = set()
        self.definitions = set()
        self.globals = []
        self.setup = []
        self.loop = []

    def add_include(
        self,
        include,
    ):

        if include:
            self.includes.add(
                str(include)
            )

    def add_definition(
        self,
        definition,
    ):

        if definition:
            self.definitions.add(
                str(definition)
            )

    def add_global(
        self,
        code,
    ):

        if code:
            self.globals.append(
                str(code)
            )

    def add_setup(
        self,
        code,
    ):

        if code:
            self.setup.append(
                str(code)
            )

    def add_loop(
        self,
        code,
    ):

        if code:
            self.loop.append(
                str(code)
            )

    def set_variable(
        self,
        name,
        value,
    ):

        if not name:
            raise ValueError(
                "Nome da variável é obrigatório."
            )

        self.variables[
            str(name)
        ] = value

        return value

    def get_variable(
        self,
        name,
        default=None,
    ):

        return self.variables.get(
            str(name),
            default,
        )

    def build(self):

        return {
            "variables": dict(
                self.variables
            ),
            "includes": sorted(
                self.includes
            ),
            "definitions": sorted(
                self.definitions
            ),
            "globals": list(
                self.globals
            ),
            "setup": list(
                self.setup
            ),
            "loop": list(
                self.loop
            ),
        }


compiler_context = CompilerContext()
