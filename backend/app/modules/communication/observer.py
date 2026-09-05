from app.modules.communication.audit_entry import (
    CommunicationAuditEntry,
)
from app.modules.communication.audit_log import (
    communication_audit_log,
)
from app.modules.communication.metrics_registry import (
    communication_metrics_registry,
)
from app.modules.communication.trace_manager import (
    communication_trace_manager,
)


class CommunicationObserver:

    def record_send(
        self,
        source: str,
        target: str | None,
        success: bool,
        details: dict | None = None,
    ):
        communication_metrics_registry.increment(
            "communication.send.total"
        )

        if success:
            communication_metrics_registry.increment(
                "communication.send.success"
            )

        else:
            communication_metrics_registry.increment(
                "communication.send.error"
            )

        communication_audit_log.add(
            CommunicationAuditEntry(
                action="send",
                source=source,
                target=target,
                success=success,
                details=dict(
                    details or {}
                ),
            )
        )

    def start_trace(
        self,
        name: str,
        metadata: dict | None = None,
    ):
        return (
            communication_trace_manager
            .start(
                name=name,
                metadata=metadata,
            )
        )

    def finish_trace(
        self,
        span_id: str,
    ):
        return (
            communication_trace_manager
            .finish(
                span_id
            )
        )


communication_observer = (
    CommunicationObserver()
)
