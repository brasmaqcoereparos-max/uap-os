from app.modules.simulator.programming.compiler.compiler_node import (
    CompilerNode,
)


class CompilerNodeFactory:

    def create(self, node):

        if node is None:
            raise ValueError(
                "Nó do compilador não informado."
            )

        return CompilerNode(node)

    def create_many(self, nodes):

        if nodes is None:
            return []

        return [
            self.create(node)
            for node in nodes
        ]


compiler_node_factory = CompilerNodeFactory()
