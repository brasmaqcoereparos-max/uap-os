from app.modules.communication.audit_log import (
    communication_audit_log,
)
from app.modules.communication.dead_letter_queue import (
    communication_dead_letter_queue,
)
from app.modules.communication.inbound_queue import (
    communication_inbound_queue,
)
from app.modules.communication.metrics_registry import (
    communication_metrics_registry,
)
from app.modules.communication.trace_manager import (
    communication_trace_manager,
)


class CommunicationObservabilityService:

    def snapshot(self):
        return {
            "metrics": (
                communication_metrics_registry
                .snapshot()
            ),
            "traces": (
                communication_trace_manager
                .list_all()
            ),
            "audit": (
                communication_audit_log
                .list_all()
            ),
            "queues": {
                "inbound": (
                    communication_inbound_queue
                    .snapshot()
                ),
                "dead_letter": {
                    "size": (
                        communication_dead_letter_queue
                        .size()
                    ),
                },
            },
        }

    def clear(self):
        communication_metrics_registry
        .clear()

        communication_trace_manager
        .clear()

        communication_audit_log
        .clear()

        return True


communication_observability_service = (
    CommunicationObservabilityService()
)
