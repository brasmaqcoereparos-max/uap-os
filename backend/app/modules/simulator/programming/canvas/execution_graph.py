from collections import defaultdict


class ExecutionGraph:

    def __init__(self):

        self.graph = defaultdict(list)

    def clear(self):

        self.graph.clear()

    def add_connection(
        self,
        source,
        target,
    ):

        if target not in self.graph[source]:

            self.graph[source].append(target)

    def remove_connection(
        self,
        source,
        target,
    ):

        if source in self.graph:

            if target in self.graph[source]:

                self.graph[source].remove(target)

    def next_nodes(
        self,
        node_id,
    ):

        return list(

            self.graph.get(

                node_id,

                [],

            )

        )

    def to_dict(self):

        return dict(self.graph)


execution_graph = ExecutionGraph()
