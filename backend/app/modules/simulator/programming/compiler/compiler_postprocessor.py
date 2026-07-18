class CompilerPostprocessor:

    def process(
        self,
        text,
    ):

        lines = []

        for line in text.splitlines():

            lines.append(

                line.rstrip()

            )

        return "\n".join(lines)


compiler_postprocessor = CompilerPostprocessor()
