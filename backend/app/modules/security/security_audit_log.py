from collections import deque

from app.modules.security.security_audit_entry import (
    SecurityAuditEntry,
)


class SecurityAuditLog:

    def __init__(
        self,
        max_size: int = 5000,
    ):
        self._entries = deque(
            maxlen=max_size
        )

    def add(
        self,
        entry: SecurityAuditEntry,
    ):
        self._entries.append(
            entry
        )

        return entry

    def list_all(self):
        return [
            entry.to_dict()
            for entry
            in self._entries
        ]

    def clear(self):
        self._entries.clear()

    def size(self):
        return len(
            self._entries
        )


security_audit_log = (
    SecurityAuditLog()
)
