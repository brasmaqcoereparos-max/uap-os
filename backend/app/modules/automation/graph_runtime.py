"""
Runtime de execução do grafo visual UAP.
"""

from app.modules.automation.graph_validator import (
    graph_validator,
)


class GraphRuntime:

    def __init__(self):
        self.active = False
        self.paused = False

        self.graph = None

        self.current_node = None
        self.current_node_id = None

        self.execution_count = 0

        self.context = {}

        self.history = []

        self.last_result = None

    def load(
        self,
        graph,
        context=None,
    ):
        if graph is None:
            raise ValueError(
                "Grafo de automação "
                "não informado."
            )

        validation = (
            graph_validator.report(
                graph
            )
        )

        if not validation["valid"]:
            raise ValueError(
                "Grafo inválido: "
                + "; ".join(
                    validation[
                        "errors"
                    ]
                )
            )

        self.graph = graph

        self.active = False
        self.paused = False

        self.current_node = None
        self.current_node_id = None

        self.execution_count = 0

        self.context = dict(
            context or {}
        )

        self.history.clear()

        self.last_result = None

        return True

    def start(self):
        if self.graph is None:
            return False

        nodes = self._nodes()

        if not nodes:
            return False

        start_id = (
            self._find_start_node_id()
        )

        if start_id is None:
            return False

        self.active = True
        self.paused = False

        self.current_node_id = (
            start_id
        )

        self.current_node = (
            nodes.get(
                start_id
            )
        )

        return True

    def stop(self):
        self.active = False
        self.paused = False

        self.current_node = None
        self.current_node_id = None

        return True

    def pause(self):
        if not self.active:
            return False

        self.paused = True

        return True

    def resume(self):
        if (
            self.graph is None
            or not self.active
        ):
            return False

        self.paused = False

        return True

    def reset(self):
        graph = self.graph

        self.active = False
        self.paused = False

        self.current_node = None
        self.current_node_id = None

        self.execution_count = 0

        self.context = {}

        self.history.clear()

        self.last_result = None

        self.graph = graph

        return True

    def execute_cycle(self):
        if not self.active:
            return None

        if self.paused:
            return None

        if self.current_node is None:
            self.stop()
            return None

        node = self.current_node

        node_id = (
            self.current_node_id
        )

        result = self._execute_node(
            node
        )

        self.execution_count += 1

        history_item = {
            "index": (
                self.execution_count
            ),
            "node_id": node_id,
            "result": result,
        }

        self.history.append(
            history_item
        )

        self.last_result = result

        self.context[
            "last_node"
        ] = node_id

        self.context[
            "last_result"
        ] = result

        next_id = self._next_node_id(
            node_id
        )

        if next_id is None:
            self.stop()

        else:
            self.current_node_id = (
                next_id
            )

            self.current_node = (
                self._nodes().get(
                    next_id
                )
            )

        return history_item

    def execute_all(
        self,
        max_cycles=10000,
    ):
        if not self.active:
            if not self.start():
                return {
                    "success": False,
                    "history": [],
                }

        cycles = 0

        while (
            self.active
            and not self.paused
            and cycles
            < int(max_cycles)
        ):
            self.execute_cycle()
            cycles += 1

        return {
            "success": (
                not self.active
            ),
            "cycles": cycles,
            "history": list(
                self.history
            ),
            "context": dict(
                self.context
            ),
        }

    def is_active(self):
        return self.active

    def status(self):
        return {
            "active": self.active,
            "paused": self.paused,
            "has_graph": (
                self.graph is not None
            ),
            "current_node": (
                self.current_node_id
            ),
            "execution_count": (
                self.execution_count
            ),
            "last_result": (
                self.last_result
            ),
        }

    def _nodes(self):
        if self.graph is None:
            return {}

        blocks = getattr(
            self.graph,
            "blocks",
            None,
        )

        if isinstance(
            blocks,
            dict,
        ):
            return blocks

        nodes = getattr(
            self.graph,
            "nodes",
            {},
        )

        if isinstance(
            nodes,
            dict,
        ):
            return nodes

        return {}

    def _connections(self):
        if self.graph is None:
            return []

        return list(
            getattr(
                self.graph,
                "connections",
                [],
            )
        )

    def _find_start_node_id(self):
        nodes = self._nodes()

        for node_id, node in (
            nodes.items()
        ):
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

            if (
                str(node_type)
                .strip()
                .lower()
                == "start"
            ):
                return str(
                    node_id
                )

        entry_method = getattr(
            self.graph,
            "entry_blocks",
            None,
        )

        if callable(
            entry_method
        ):
            entries = (
                entry_method()
            )

            if entries:
                return str(
                    entries[0]
                )

        return next(
            iter(nodes.keys()),
            None,
        )

    def _next_node_id(
        self,
        node_id,
    ):
        expected = str(
            node_id
        )

        for connection in (
            self._connections()
        ):
            if isinstance(
                connection,
                dict,
            ):
                source = (
                    connection.get(
                        "source"
                    )
                )

                target = (
                    connection.get(
                        "target"
                    )
                )

                enabled = (
                    connection.get(
                        "enabled",
                        True,
                    )
                )

            else:
                source = getattr(
                    connection,
                    "source",
                    None,
                )

                target = getattr(
                    connection,
                    "target",
                    None,
                )

                enabled = getattr(
                    connection,
                    "enabled",
                    True,
                )

            if not enabled:
                continue

            if str(source) == expected:
                return str(
                    target
                )

        return None

    def _execute_node(
        self,
        node,
    ):
        if not getattr(
            node,
            "enabled",
            True,
        ):
            return {
                "executed": False,
                "reason": "disabled",
            }

        execute = getattr(
            node,
            "execute",
            None,
        )

        if callable(execute):
            try:
                return execute(
                    self.context
                )

            except TypeError:
                return execute()

        run = getattr(
            node,
            "run",
            None,
        )

        if callable(run):
            try:
                return run(
                    self.context
                )

            except TypeError:
                return run()

        return None


graph_runtime = GraphRuntime()
