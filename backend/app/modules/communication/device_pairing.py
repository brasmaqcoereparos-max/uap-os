from __future__ import annotations

import secrets
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class PairingSession:
    session_id: str
    device_id: str
    code: str
    created_at: datetime
    confirmed: bool = False


class DevicePairingManager:
    def __init__(self) -> None:
        self._sessions: dict[
            str,
            PairingSession,
        ] = {}

    def create(
        self,
        device_id: str,
    ) -> PairingSession:
        session_id = secrets.token_hex(16)
        code = f"{secrets.randbelow(1000000):06d}"

        session = PairingSession(
            session_id=session_id,
            device_id=device_id,
            code=code,
            created_at=datetime.now(timezone.utc),
        )

        self._sessions[session_id] = session

        return session

    def confirm(
        self,
        session_id: str,
        code: str,
    ) -> bool:
        session = self._sessions.get(session_id)

        if session is None:
            return False

        if not secrets.compare_digest(
            session.code,
            str(code),
        ):
            return False

        session.confirmed = True
        return True

    def get(
        self,
        session_id: str,
    ) -> PairingSession | None:
        return self._sessions.get(session_id)

    def remove(
        self,
        session_id: str,
    ) -> bool:
        return self._sessions.pop(
            session_id,
            None,
        ) is not None
