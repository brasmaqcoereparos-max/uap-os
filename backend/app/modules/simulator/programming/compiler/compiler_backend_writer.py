class CompilerBackendWriter:

    def __init__(self):

        self.lines = []

    def write(self, line=""):

        self.lines.append(line)

    def extend(self, lines):

        self.lines.extend(lines)

    def blank(self):

        self.lines.append("")

    def build(self):

        return "\n".join(self.lines)

    def clear(self):

        self.lines.clear()


compiler_backend_writer = CompilerBackendWriter()
