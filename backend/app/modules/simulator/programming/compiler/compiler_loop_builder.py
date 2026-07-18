class CompilerLoopBuilder:

    def build(
        self,
        loop,
    ):

        lines = []

        lines.append("void loop() {")

        for line in loop:

            lines.append(f"    {line}")

        lines.append("}")

        return lines


compiler_loop_builder = CompilerLoopBuilder()
