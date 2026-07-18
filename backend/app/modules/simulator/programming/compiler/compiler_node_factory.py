from app.modules.simulator.programming.compiler.compiler_node import (
    CompilerNode,
)


class CompilerNodeFactory:

    def create(self, node):

        return CompilerNode(node)


compiler_node_factory = CompilerNodeFactory()
