"""
Runtime de execução do grafo de automação UAP.
"""

from __future__ import annotations


class GraphRuntime:

    def __init__(self):

        self.active = False
        self.graph = None
        self.current_node = None
        self.execution_count = 0

    def load(
        self,
        graph,
    ):

        if graph is None:
            raise ValueError(
                "Grafo de automação não informado."
            )

        self.graph = graph
        self.active = False
        self.current_node = None
        self.execution_count = 0

    def start(self):

        if self.graph is None:
            return False

        if not getattr(
            self.graph,
            "nodes",
            None,
        ):

            return False

        self.active = True

        self.current_node = (
            self._find_start_node()
        )

        return True

    def stop(self):

        self.active = False
        self.current_node = None

    def pause(self):

        if self.active:
            self.active = False

    def resume(self):

        if self.graph is None:
            return False

        self.active = True

        if self.current_node is None:
            self.current_node = (
                self._find_start_node()
            )

        return True

    def execute_cycle(self):

        if not self.active:
            return None

        if self.current_node is None:

            self.stop()

            return None

        node = self.current_node

        self.execution_count += 1

        self.current_node = (
            self._next_node(
                node
            )
        )

        if self.current_node is None:
            self.active = False

        return node

    def is_active(self):

        return self.active

    def status(self):

        return {
            "active": self.active,
            "has_graph": self.graph is not None,
            "current_node": (
                self._node_id(
                    self.current_node
                )
            ),
            "execution_count": (
                self.execution_count
            ),
        }

    def _find_start_node(self):

        nodes = getattr(
            self.graph,
            "nodes",
            {},
        )

        for node in nodes.values():

            node_type = (
                getattr(
                    node,
                    "node_type",
                    None,
                )
                or getattr(
                    node,
                    "type",
                    None,
                )
                or getattr(
                    node,
                    "block_type",
                    None,
                )
                or ""
            )

            if str(
                node_type
            ).lower() == "start":

                return node

        return next(
            iter(
                nodes.values()
            ),
            None,
        )

    def _next_node(
        self,
        node,
    ):

        connections = getattr(
            self.graph,
            "connections",
            [],
        )

        node_id = self._node_id(
            node
        )

        for connection in connections:

            source = getattr(
                connection,
                "source_node",
                None,
            )

            source_id = self._node_id(
                source
            )

            if source_id != node_id:
                continue

            target = getattr(
                connection,
                "target_node",
                None,
            )

            if target is not None:
                return target

        return None

    @staticmethod
    def _node_id(
        node,
    ):

        if node is None:
            return None

        return (
            getattr(
                node,
                "node_id",
                None,
            )
            or getattr(
                node,
                "id",
                None,
            )
        )


graph_runtime = GraphRuntime()
