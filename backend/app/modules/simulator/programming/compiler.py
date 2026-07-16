from collections import deque

from app.modules.simulator.programming.canvas.canvas import canvas


class BlockCompiler:

    def build_graph(self):

        graph = {}

        for node in canvas.all_nodes():

            graph[node.id] = {
                "node": node,
                "next": [],
                "previous": [],
            }

        for connection in canvas.all_connections():

            if connection.source in graph and connection.target in graph:

                graph[connection.source]["next"].append(
                    connection.target
                )

                graph[connection.target]["previous"].append(
                    connection.source
                )

        return graph

    def execution_order(self):

        graph = self.build_graph()

        indegree = {
            node: len(data["previous"])
            for node, data in graph.items()
        }

        queue = deque(
            [
                node
                for node, value in indegree.items()
                if value == 0
            ]
        )

        order = []

        while queue:

            current = queue.popleft()

            order.append(graph[current]["node"])

            for nxt in graph[current]["next"]:

                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    queue.append(nxt)

        return order

    def compile(self):

        order = self.execution_order()

        return {
            "compiled": True,
            "nodes": len(order),
            "execution_order": [
                node.to_dict()
                for node in order
            ],
        }


compiler = BlockCompiler()
