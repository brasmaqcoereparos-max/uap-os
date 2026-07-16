from app.modules.simulator.programming.canvas.canvas import canvas


class BaseGenerator:

    LANGUAGE = "TEXT"

    def header(self):
        return ""

    def footer(self):
        return ""

    def generate_node(self, node):
        return f"// {node.name}"

    def get_execution_order(self):
        """
        Percorre o Canvas seguindo as conexões.
        Caso não existam conexões, utiliza a ordem
        de criação dos nós.
        """

        if not canvas.connections:
            return list(canvas.nodes.values())

        incoming = {
            node_id: 0
            for node_id in canvas.nodes
        }

        for connection in canvas.connections:
            incoming[connection.target] = (
                incoming.get(connection.target, 0) + 1
            )

        roots = [
            canvas.nodes[node_id]
            for node_id, count in incoming.items()
            if count == 0
        ]

        visited = set()

        ordered = []

        def visit(node):

            if node.id in visited:
                return

            visited.add(node.id)

            ordered.append(node)

            for connection in canvas.connections:

                if connection.source == node.id:

                    target = canvas.nodes.get(
                        connection.target
                    )

                    if target:
                        visit(target)

        for root in roots:
            visit(root)

        for node in canvas.nodes.values():

            if node.id not in visited:
                ordered.append(node)

        return ordered

    def generate(self):

        code = []

        header = self.header()

        if header:
            code.append(header)

        for node in self.get_execution_order():

            code.append(
                self.generate_node(node)
            )

        footer = self.footer()

        if footer:
            code.append(footer)

        return "\n".join(code)
