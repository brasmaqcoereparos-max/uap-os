class CompilerEmitter:

    def __init__(self):

        self.output = []

    def emit(
        self,
        line="",
    ):

        self.output.append(line)

    def emit_many(
        self,
        lines,
    ):

        self.output.extend(lines)

    def newline(self):

        self.output.append("")

    def clear(self):

        self.output.clear()

    def build(self):

        return "\n".join(self.output)


compiler_emitter = CompilerEmitter()
