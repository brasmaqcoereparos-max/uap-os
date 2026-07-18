class CompilerFormatter:

    def indent(

        self,

        text,

        spaces=4,

    ):

        prefix = " " * spaces

        return "\n".join(

            prefix + line

            if line

            else ""

            for line in text.splitlines()

        )

    def trim(self, text):

        return text.strip()


compiler_formatter = CompilerFormatter()
