from app.modules.communication.connection_manager import (
    communication_connection_manager,
)
from app.modules.communication.retry_executor import (
    communication_retry_executor,
)
from app.modules.communication.retry_policy import (
    CommunicationRetryPolicy,
)
from app.modules.communication.session_manager import (
    communication_session_manager,
)
from app.modules.communication.transport_manager import (
    communication_transport_manager,
)


class CommunicationConnectionService:

    def open(
        self,
        transport: str,
        destination: str,
    ):
        selected = (
            communication_transport_manager
            .get(transport)
        )

        connection = (
            communication_connection_manager
            .create(
                transport=selected.name,
                destination=destination,
            )
        )

        connection.connect()

        session = (
            communication_session_manager
            .create(
                connection_id=(
                    connection.id
                )
            )
        )

        return {
            "connection": (
                connection.to_dict()
            ),
            "session": (
                session.to_dict()
            ),
        }

    def send(
        self,
        connection_id: str,
        payload: dict,
        retry_policy: (
            CommunicationRetryPolicy
            | None
        ) = None,
    ):
        connection = (
            communication_connection_manager
            .get(
                connection_id
            )
        )

        if not connection:
            raise ValueError(
                "Communication connection "
                "not found"
            )

        def operation():
            result = (
                communication_transport_manager
                .send(
                    destination=(
                        connection.destination
                    ),
                    payload=payload,
                    transport_name=(
                        connection.transport
                    ),
                )
            )

            connection.touch()

            return result.to_dict()

        return (
            communication_retry_executor
            .execute(
                operation=operation,
                policy=retry_policy,
            )
        )

    def close(
        self,
        connection_id: str,
    ):
        connection = (
            communication_connection_manager
            .disconnect(
                connection_id
            )
        )

        if not connection:
            return False

        for session in (
            communication_session_manager
            .active()
        ):
            if (
                session.connection_id
                == connection_id
            ):
                communication_session_manager
                .close(
                    session.id
                )

        return True


communication_connection_service = (
    CommunicationConnectionService()
              )
