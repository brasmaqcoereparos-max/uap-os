class CompilerContext:

    def __init__(self):

        self.variables = {}

        self.includes = set()

        self.definitions = set()

        self.globals = []

        self.setup = []

        self.loop = []

    def add_include(self, include):

        self.includes.add(include)

    def add_definition(self, definition):

        self.definitions.add(definition)

    def add_global(self, code):

        self.globals.append(code)

    def add_setup(self, code):

        self.setup.append(code)

    def add_loop(self, code):

        self.loop.append(code)

    def set_variable(self, name, value):

        self.variables[name] = value

    def get_variable(self, name, default=None):

        return self.variables.get(name, default)

    def build(self):

        return {

            "includes": sorted(self.includes),

            "definitions": sorted(self.definitions),

            "globals": self.globals,

            "setup": self.setup,

            "loop": self.loop,

        }


compiler_context = CompilerContext()
