from app.modules.automation.block_connection import (
    BlockConnection,
)


class BlockFlow:

    def __init__(self):
        self.connections = []

    def connect(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
        metadata=None,
    ):
        connection = BlockConnection(
            source=source,
            target=target,
            source_port=source_port,
            target_port=target_port,
            metadata=metadata,
        )

        if not self.exists(
            source,
            target,
            source_port,
            target_port,
        ):
            self.connections.append(
                connection
            )

        return connection

    def disconnect(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        before = len(
            self.connections
        )

        self.connections = [
            item
            for item in self.connections
            if not item.matches(
                source,
                target,
                source_port,
                target_port,
            )
        ]

        return (
            len(self.connections)
            != before
        )

    def exists(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        return any(
            item.matches(
                source,
                target,
                source_port,
                target_port,
            )
            for item
            in self.connections
        )

    def incoming(
        self,
        target,
    ):
        target = str(target)

        return [
            item
            for item in self.connections
            if item.target == target
        ]

    def outgoing(
        self,
        source,
    ):
        source = str(source)

        return [
            item
            for item in self.connections
            if item.source == source
        ]

    def clear(self):
        self.connections.clear()

    def get_connections(
        self,
        serialized=True,
    ):
        if serialized:
            return [
                item.to_dict()
                for item
                in self.connections
            ]

        return list(
            self.connections
        )

    def count(self):
        return len(
            self.connections
        )

    def to_dict(self):
        return {
            "connections": (
                self.get_connections()
            ),
            "count": self.count(),
        }
