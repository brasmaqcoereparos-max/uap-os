from app.modules.simulator.programming.compiler import (
    compiler,
)


class BaseGenerator:

    LANGUAGE = "TEXT"

    def header(self):
        return ""

    def footer(self):
        return ""

    def generate_node(self, node):
        return f"// {node.name}"

    def generate(self):

        lines = []

        header = self.header()

        if header:
            lines.append(header)

        execution = compiler.execution_order()

        for node in execution:

            lines.append(
                self.generate_node(node)
            )

        footer = self.footer()

        if footer:
            lines.append(footer)

        return "\n".join(lines)
