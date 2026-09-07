from app.modules.security.security_audit_log import (
    security_audit_log,
)
from app.modules.security.security_event_log import (
    security_event_log,
)
from app.modules.security.security_session_manager import (
    security_session_manager,
)


class SecurityProtectionStatus:

    def snapshot(self):
        return {
            "service": (
                "security-protection"
            ),
            "healthy": True,
            "active_sessions": [
                session.to_dict()
                for session
                in security_session_manager
                .active()
            ],
            "audit_entries": (
                security_audit_log
                .size()
            ),
            "security_events": (
                security_event_log
                .size()
            ),
        }


security_protection_status = (
    SecurityProtectionStatus()
)
