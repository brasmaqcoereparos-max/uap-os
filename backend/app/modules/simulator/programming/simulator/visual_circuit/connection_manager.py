"""
Gerenciador de conexões do circuito visual UAP.
"""

from app.modules.simulator.programming.simulator.visual_circuit.connection import (
    Connection,
)


class ConnectionManager:

    def __init__(self):
        self.connections = []

    def add(
        self,
        connection,
        prevent_duplicate=True,
    ):
        if not isinstance(
            connection,
            Connection,
        ):
            raise TypeError(
                "connection precisa "
                "ser uma Connection."
            )

        if (
            prevent_duplicate
            and self.exists(
                connection.source,
                connection.source_pin,
                connection.target,
                connection.target_pin,
            )
        ):
            return self.find(
                connection.source,
                connection.source_pin,
                connection.target,
                connection.target_pin,
            )

        self.connections.append(
            connection
        )

        return connection

    def connect(
        self,
        source,
        source_pin,
        target,
        target_pin,
        metadata=None,
    ):
        connection = Connection(
            source=source,
            source_pin=source_pin,
            target=target,
            target_pin=target_pin,
            metadata=metadata,
        )

        return self.add(
            connection
        )

    def remove(
        self,
        connection,
    ):
        if connection in (
            self.connections
        ):
            self.connections.remove(
                connection
            )

            return True

        return False

    def remove_by_id(
        self,
        connection_id,
    ):
        connection_id = str(
            connection_id
        )

        for connection in list(
            self.connections
        ):
            if (
                str(connection.id)
                == connection_id
            ):
                self.connections.remove(
                    connection
                )

                return True

        return False

    def remove_component(
        self,
        component,
    ):
        before = len(
            self.connections
        )

        self.connections = [
            connection
            for connection
            in self.connections
            if not connection.involves(
                component
            )
        ]

        return (
            before
            - len(self.connections)
        )

    def find(
        self,
        source,
        source_pin,
        target,
        target_pin,
    ):
        for connection in (
            self.connections
        ):
            if connection.matches(
                source,
                source_pin,
                target,
                target_pin,
            ):
                return connection

        return None

    def exists(
        self,
        source,
        source_pin,
        target,
        target_pin,
    ):
        return (
            self.find(
                source,
                source_pin,
                target,
                target_pin,
            )
            is not None
        )

    def incoming(
        self,
        component,
    ):
        component_id = (
            Connection._component_id(
                component
            )
        )

        return [
            connection
            for connection
            in self.connections
            if (
                connection.target_id
                == component_id
            )
        ]

    def outgoing(
        self,
        component,
    ):
        component_id = (
            Connection._component_id(
                component
            )
        )

        return [
            connection
            for connection
            in self.connections
            if (
                connection.source_id
                == component_id
            )
        ]

    def all(self):
        return self.connections.copy()

    def enabled(self):
        return [
            connection
            for connection
            in self.connections
            if connection.enabled
        ]

    def clear(self):
        count = len(
            self.connections
        )

        self.connections.clear()

        return count

    def count(self):
        return len(
            self.connections
        )

    def to_dict(self):
        return [
            connection.to_dict()
            for connection
            in self.connections
        ]


connection_manager = (
    ConnectionManager()
        )
