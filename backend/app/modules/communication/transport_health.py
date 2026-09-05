from app.modules.communication.connection_manager import (
    communication_connection_manager,
)
from app.modules.communication.session_manager import (
    communication_session_manager,
)
from app.modules.communication.transport_manager import (
    communication_transport_manager,
)


class CommunicationTransportHealth:

    def check(self):
        transports = (
            communication_transport_manager
            .transports()
        )

        connections = (
            communication_connection_manager
            .list_all()
        )

        sessions = (
            communication_session_manager
            .active()
        )

        return {
            "healthy": True,
            "transports": transports,
            "connections": [
                connection.to_dict()
                for connection
                in connections
            ],
            "active_sessions": [
                session.to_dict()
                for session
                in sessions
            ],
        }


communication_transport_health = (
    CommunicationTransportHealth()
)
