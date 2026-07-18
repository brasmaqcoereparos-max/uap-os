class CompilerWriter:

    def __init__(self):

        self.lines = []

    def write(self, text=""):

        self.lines.append(text)

    def blank(self):

        self.lines.append("")

    def extend(self, values):

        self.lines.extend(values)

    def build(self):

        return "\n".join(self.lines)

    def clear(self):

        self.lines.clear()


compiler_writer = CompilerWriter()
