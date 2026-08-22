"""
Compilador principal dos blocos visuais do UAP.

Converte o Canvas em uma ordem de execução determinística
e fornece uma representação serializável do programa.
"""

from collections import deque


class BlockCompiler:

    def __init__(self):
        self.last_graph = {}
        self.last_order = []

    def build_graph(self, canvas):

        if canvas is None:
            raise ValueError(
                "Canvas é obrigatório."
            )

        graph = {}

        for node in canvas.all_nodes():

            graph[node.id] = {
                "node": node,
                "next": [],
                "previous": [],
            }

        for connection in canvas.all_connections():

            source = connection.source
            target = connection.target

            if source not in graph:
                continue

            if target not in graph:
                continue

            if target not in graph[source]["next"]:
                graph[source]["next"].append(
                    target
                )

            if source not in graph[target]["previous"]:
                graph[target]["previous"].append(
                    source
                )

        self.last_graph = graph

        return graph

    def execution_order(self, canvas):

        graph = self.build_graph(canvas)

        indegree = {
            node_id: len(data["previous"])
            for node_id, data in graph.items()
        }

        queue = deque(
            node_id
            for node_id, degree in indegree.items()
            if degree == 0
        )

        order = []

        while queue:

            current = queue.popleft()

            order.append(
                graph[current]["node"]
            )

            for nxt in graph[current]["next"]:

                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    queue.append(nxt)

        if len(order) != len(graph):

            remaining = [
                node_id
                for node_id, degree in indegree.items()
                if degree > 0
            ]

            raise ValueError(
                "O grafo do programa contém um ciclo "
                "ou conexões inválidas: "
                + ", ".join(
                    remaining
                )
            )

        self.last_order = order

        return order

    def compile(self, canvas):

        order = self.execution_order(
            canvas
        )

        return {
            "compiled": True,
            "nodes": len(order),
            "execution_order": [
                node.to_dict()
                for node in order
            ],
        }


compiler = BlockCompiler()
