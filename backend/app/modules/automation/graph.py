class AutomationGraph:
    def __init__(self):
        self.nodes = {}
        self.connections = []

    @property
    def blocks(self):
        return self.nodes

    @staticmethod
    def _node_id(node):
        node_id = getattr(
            node,
            "node_id",
            None,
        )

        if node_id is None:
            node_id = getattr(
                node,
                "block_id",
                None,
            )

        if node_id is None:
            raise ValueError(
                "Nó sem node_id/block_id."
            )

        return str(node_id)

    @staticmethod
    def _connection_source(
        connection,
    ):
        if isinstance(
            connection,
            dict,
        ):
            return str(
                connection.get(
                    "source",
                    ""
                )
            )

        source = getattr(
            connection,
            "source",
            None,
        )

        if source is not None:
            return str(source)

        source_node = getattr(
            connection,
            "source_node",
            None,
        )

        if source_node is None:
            return ""

        return str(
            getattr(
                source_node,
                "node_id",
                getattr(
                    source_node,
                    "block_id",
                    source_node,
                ),
            )
        )

    @staticmethod
    def _connection_target(
        connection,
    ):
        if isinstance(
            connection,
            dict,
        ):
            return str(
                connection.get(
                    "target",
                    ""
                )
            )

        target = getattr(
            connection,
            "target",
            None,
        )

        if target is not None:
            return str(target)

        target_node = getattr(
            connection,
            "target_node",
            None,
        )

        if target_node is None:
            return ""

        return str(
            getattr(
                target_node,
                "node_id",
                getattr(
                    target_node,
                    "block_id",
                    target_node,
                ),
            )
        )

    def add_node(
        self,
        node,
    ):
        node_id = self._node_id(
            node
        )

        self.nodes[
            node_id
        ] = node

        return node_id

    def add_block(
        self,
        block,
    ):
        return self.add_node(
            block
        )

    def remove_node(
        self,
        node_id,
    ):
        node_id = str(
            node_id
        )

        removed = self.nodes.pop(
            node_id,
            None,
        )

        self.connections = [
            connection
            for connection
            in self.connections
            if (
                self._connection_source(
                    connection
                )
                != node_id
                and self._connection_target(
                    connection
                )
                != node_id
            )
        ]

        return removed is not None

    def remove_block(
        self,
        block_id,
    ):
        return self.remove_node(
            block_id
        )

    def connect(
        self,
        connection=None,
        source=None,
        target=None,
        source_port=None,
        target_port=None,
    ):
        if connection is None:
            if (
                source is None
                or target is None
            ):
                raise ValueError(
                    "source e target "
                    "são obrigatórios."
                )

            connection = {
                "source": str(source),
                "target": str(target),
                "source_port": (
                    source_port
                ),
                "target_port": (
                    target_port
                ),
                "enabled": True,
            }

        self.connections.append(
            connection
        )

        return connection

    def disconnect(
        self,
        source,
        target,
    ):
        source = str(source)
        target = str(target)

        before = len(
            self.connections
        )

        self.connections = [
            connection
            for connection
            in self.connections
            if not (
                self._connection_source(
                    connection
                )
                == source
                and self._connection_target(
                    connection
                )
                == target
            )
        ]

        return (
            len(self.connections)
            != before
        )

    def get_node(
        self,
        node_id,
    ):
        return self.nodes.get(
            str(node_id)
        )

    def get_block(
        self,
        block_id,
    ):
        return self.get_node(
            block_id
        )

    def list_nodes(self):
        return list(
            self.nodes.values()
        )

    def list_connections(self):
        return list(
            self.connections
        )

    def incoming(
        self,
        node_id,
    ):
        node_id = str(node_id)

        return [
            connection
            for connection
            in self.connections
            if (
                self._connection_target(
                    connection
                )
                == node_id
            )
        ]

    def outgoing(
        self,
        node_id,
    ):
        node_id = str(node_id)

        return [
            connection
            for connection
            in self.connections
            if (
                self._connection_source(
                    connection
                )
                == node_id
            )
        ]

    def entry_blocks(self):
        targets = {
            self._connection_target(
                connection
            )
            for connection
            in self.connections
        }

        return [
            node_id
            for node_id
            in self.nodes
            if node_id not in targets
        ]

    def to_dict(self):
        return {
            "nodes": {
                node_id: (
                    node.to_dict()
                    if hasattr(
                        node,
                        "to_dict",
                    )
                    else str(node)
                )
                for node_id, node
                in self.nodes.items()
            },
            "connections": [
                (
                    connection
                    if isinstance(
                        connection,
                        dict,
                    )
                    else connection.to_dict()
                    if hasattr(
                        connection,
                        "to_dict",
                    )
                    else str(connection)
                )
                for connection
                in self.connections
            ],
            }
