class CompilerOptimizer:

    def optimize(self, nodes):

        optimized = []

        visited = set()

        for node in nodes:

            node_id = node["id"]

            if node_id in visited:

                continue

            visited.add(node_id)

            optimized.append(node)

        return optimized


compiler_optimizer = CompilerOptimizer()
