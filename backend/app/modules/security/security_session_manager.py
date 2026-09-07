import uuid

from app.modules.security.security_session import (
    SecuritySession,
)


class SecuritySessionManager:

    def __init__(self):
        self._sessions: dict[
            str,
            SecuritySession,
        ] = {}

    def create(
        self,
        principal_id: str,
        metadata: dict | None = None,
    ):
        session = SecuritySession(
            session_id=str(
                uuid.uuid4()
            ),
            principal_id=principal_id,
            metadata=dict(
                metadata or {}
            ),
        )

        self._sessions[
            session.session_id
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
            return False

        session.close()

        return True

    def active(self):
        return [
            session
            for session
            in self._sessions.values()
            if session.active
        ]


security_session_manager = (
    SecuritySessionManager()
    )
