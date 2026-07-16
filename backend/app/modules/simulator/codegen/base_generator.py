from app.modules.simulator.programming.canvas.canvas import canvas


class BaseGenerator:

    LANGUAGE = "TEXT"

    def header(self):
        return ""

    def footer(self):
        return ""

    def generate_node(self, node):
        return f"// {node.name}"

    def generate(self):

        code = []

        header = self.header()

        if header:
            code.append(header)

        for node in canvas.nodes.values():
            code.append(
                self.generate_node(node)
            )

        footer = self.footer()

        if footer:
            code.append(footer)

        return "\n".join(code)
