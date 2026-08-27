from collections import deque
from typing import Any


class BlockGraph:

    def __init__(self):
        self.blocks: dict[str, Any] = {}
        self.connections: list[dict[str, Any]] = []

    @property
    def nodes(self):
        # Compatibilidade com componentes que usam graph.nodes.
        return self.blocks

    def add_block(
        self,
        block_id,
        block,
    ):
        block_id = str(block_id).strip()

        if not block_id:
            raise ValueError(
                "block_id é obrigatório."
            )

        if block is None:
            raise ValueError(
                "Bloco inválido."
            )

        if block_id in self.blocks:
            raise ValueError(
                f"Bloco '{block_id}' já existe."
            )

        self.blocks[block_id] = block

        return block

    def remove_block(
        self,
        block_id,
    ):
        block_id = str(block_id)

        removed = self.blocks.pop(
            block_id,
            None,
        )

        if removed is None:
            return False

        self.connections = [
            connection
            for connection in self.connections
            if connection.get("source") != block_id
            and connection.get("target") != block_id
        ]

        return True

    def get_block(
        self,
        block_id,
    ):
        return self.blocks.get(
            str(block_id)
        )

    def has_block(
        self,
        block_id,
    ):
        return str(block_id) in self.blocks

    def connect(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
        metadata=None,
    ):
        source = str(source)
        target = str(target)

        if source not in self.blocks:
            return False

        if target not in self.blocks:
            return False

        connection = {
            "source": source,
            "target": target,
            "source_port": source_port,
            "target_port": target_port,
            "metadata": dict(
                metadata or {}
            ),
        }

        if connection in self.connections:
            return True

        self.connections.append(
            connection
        )

        return True

    def disconnect(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        source = str(source)
        target = str(target)

        original = len(
            self.connections
        )

        self.connections = [
            connection
            for connection in self.connections
            if not (
                connection.get("source") == source
                and connection.get("target") == target
                and (
                    source_port is None
                    or connection.get(
                        "source_port"
                    ) == source_port
                )
                and (
                    target_port is None
                    or connection.get(
                        "target_port"
                    ) == target_port
                )
            )
        ]

        return (
            len(self.connections)
            != original
        )

    def clear_connections(self):
        self.connections.clear()

    def clear(self):
        self.blocks.clear()
        self.connections.clear()

    def get_blocks(self):
        return dict(self.blocks)

    def get_connections(self):
        return [
            dict(connection)
            for connection
            in self.connections
        ]

    def incoming(
        self,
        block_id,
    ):
        block_id = str(block_id)

        return [
            dict(connection)
            for connection in self.connections
            if connection.get("target")
            == block_id
        ]

    def outgoing(
        self,
        block_id,
    ):
        block_id = str(block_id)

        return [
            dict(connection)
            for connection in self.connections
            if connection.get("source")
            == block_id
        ]

    def entry_blocks(self):
        targets = {
            connection.get("target")
            for connection
            in self.connections
        }

        return [
            block_id
            for block_id
            in self.blocks
            if block_id not in targets
        ]

    def topological_order(self):
        indegree = {
            block_id: 0
            for block_id in self.blocks
        }

        adjacency = {
            block_id: []
            for block_id in self.blocks
        }

        for connection in self.connections:
            source = connection.get(
                "source"
            )
            target = connection.get(
                "target"
            )

            if (
                source not in self.blocks
                or target not in self.blocks
            ):
                continue

            adjacency[source].append(
                target
            )

            indegree[target] += 1

        queue = deque(
            block_id
            for block_id, degree
            in indegree.items()
            if degree == 0
        )

        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for target in adjacency[current]:
                indegree[target] -= 1

                if indegree[target] == 0:
                    queue.append(target)

        if len(result) != len(
            self.blocks
        ):
            return []

        return result

    def has_cycle(self):
        if not self.blocks:
            return False

        return not bool(
            self.topological_order()
        )

    def to_dict(self):
        blocks = {}

        for block_id, block in (
            self.blocks.items()
        ):
            serializer = getattr(
                block,
                "to_dict",
                None,
            )

            if callable(serializer):
                blocks[block_id] = (
                    serializer()
                )
            else:
                blocks[block_id] = {
                    "value": str(block)
                }

        return {
            "blocks": blocks,
            "connections": (
                self.get_connections()
            ),
        }
