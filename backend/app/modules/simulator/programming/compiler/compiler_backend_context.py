class CompilerBackendContext:

    def __init__(self):

        self.reset()

    def reset(self):

        self.headers = []

        self.globals = []

        self.setup = []

        self.loop = []

        self.functions = []

    def add_header(self, line):

        self.headers.append(line)

    def add_global(self, line):

        self.globals.append(line)

    def add_setup(self, line):

        self.setup.append(line)

    def add_loop(self, line):

        self.loop.append(line)

    def add_function(self, line):

        self.functions.append(line)


compiler_backend_context = CompilerBackendContext()
