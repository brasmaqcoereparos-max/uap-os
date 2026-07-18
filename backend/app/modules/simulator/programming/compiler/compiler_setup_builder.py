class CompilerSetupBuilder:

    def build(
        self,
        setup,
    ):

        lines = []

        lines.append("void setup() {")

        for line in setup:

            lines.append(f"    {line}")

        lines.append("}")

        return lines


compiler_setup_builder = CompilerSetupBuilder()
