from app.modules.communication.channel_registry import (
    communication_channel_registry,
)
from app.modules.communication.connection_manager import (
    communication_connection_manager,
)
from app.modules.communication.session_manager import (
    communication_session_manager,
)
from app.modules.communication.transport_health import (
    communication_transport_health,
)


class CommunicationStatus:

    def snapshot(self):
        return {
            "service": (
                "communication"
            ),
            "healthy": True,
            "channels": [
                channel.to_dict()
                for channel
                in communication_channel_registry
                .list_all()
            ],
            "connections": [
                connection.to_dict()
                for connection
                in communication_connection_manager
                .list_all()
            ],
            "sessions": [
                session.to_dict()
                for session
                in communication_session_manager
                .active()
            ],
            "transport_health": (
                communication_transport_health
                .check()
            ),
        }


communication_status = (
    CommunicationStatus()
)
