import uuid

from app.modules.communication.session import (
    CommunicationSession,
)


class CommunicationSessionManager:

    def __init__(self):
        self._sessions: dict[
            str,
            CommunicationSession,
        ] = {}

    def create(
        self,
        connection_id: str,
    ):
        session = CommunicationSession(
            id=str(uuid.uuid4()),
            connection_id=connection_id,
        )

        self._sessions[
            session.id
        ] = session

        return session

    def get(
        self,
        session_id: str,
    ):
        return self._sessions.get(
            session_id
        )

    def close(
        self,
        session_id: str,
    ):
        session = self.get(
            session_id
        )

        if not session:
            return None

        session.close()

        return session

    def remove(
        self,
        session_id: str,
    ):
        return self._sessions.pop(
            session_id,
            None,
        )

    def active(self):
        return [
            session
            for session
            in self._sessions.values()
            if session.active
        ]


communication_session_manager = (
    CommunicationSessionManager()
          )
