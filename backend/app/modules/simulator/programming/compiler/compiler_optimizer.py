"""
Otimizador básico do compilador UAP.
"""


class CompilerOptimizer:

    def optimize(self, nodes):

        if nodes is None:
            return []

        optimized = []
        visited = set()

        for node in nodes:

            if not isinstance(
                node,
                dict,
            ):
                continue

            node_id = node.get("id")

            if node_id is None:
                continue

            if node_id in visited:
                continue

            visited.add(node_id)

            optimized.append(
                dict(node)
            )

        return optimized


compiler_optimizer = CompilerOptimizer()
