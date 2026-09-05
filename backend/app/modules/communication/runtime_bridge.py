from typing import Any

from app.modules.communication.communication_facade import (
    communication_facade,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)


class CommunicationRuntimeBridge:

    def publish_runtime_event(
        self,
        source: str,
        event: str,
        payload: dict[str, Any] | None = None,
    ):
        return communication_facade.publish(
            topic=communication_topics.RUNTIME_EVENT,
            source=source,
            payload={
                "event": event,
                "payload": dict(
                    payload or {}
                ),
            },
        )


communication_runtime_bridge = (
    CommunicationRuntimeBridge()
)
