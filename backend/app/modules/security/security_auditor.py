from app.modules.security.security_audit_entry import (
    SecurityAuditEntry,
)
from app.modules.security.security_audit_log import (
    security_audit_log,
)


class SecurityAuditor:

    def record(
        self,
        action: str,
        success: bool,
        source: str = "security",
        target: str | None = None,
        details: dict | None = None,
    ):
        entry = SecurityAuditEntry(
            action=action,
            success=success,
            source=source,
            target=target,
            details=dict(
                details or {}
            ),
        )

        return (
            security_audit_log
            .add(entry)
        )


security_auditor = (
    SecurityAuditor()
)
