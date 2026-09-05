import uuid

from app.modules.communication.connection import (
    CommunicationConnection,
)


class CommunicationConnectionManager:

    def __init__(self):
        self._connections: dict[
            str,
            CommunicationConnection,
        ] = {}

    def create(
        self,
        transport: str,
        destination: str,
    ):
        connection = (
            CommunicationConnection(
                id=str(uuid.uuid4()),
                transport=transport,
                destination=destination,
            )
        )

        self._connections[
            connection.id
        ] = connection

        return connection

    def get(
        self,
        connection_id: str,
    ):
        return self._connections.get(
            connection_id
        )

    def connect(
        self,
        connection_id: str,
    ):
        connection = self.get(
            connection_id
        )

        if not connection:
            raise ValueError(
                "Communication connection "
                "not found"
            )

        return connection.connect()

    def disconnect(
        self,
        connection_id: str,
    ):
        connection = self.get(
            connection_id
        )

        if not connection:
            return None

        return connection.disconnect()

    def remove(
        self,
        connection_id: str,
    ):
        return self._connections.pop(
            connection_id,
            None,
        )

    def list_all(self):
        return list(
            self._connections.values()
        )


communication_connection_manager = (
    CommunicationConnectionManager()
)
