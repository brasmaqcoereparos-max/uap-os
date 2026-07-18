class CompilerLinker:

    def link(
        self,
        sections,
    ):

        output = []

        for section in sections:

            if section:

                output.append(section)

        return "\n\n".join(output)


compiler_linker = CompilerLinker()
