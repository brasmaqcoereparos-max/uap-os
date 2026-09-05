from typing import Any

from app.modules.communication.communication_facade import (
    communication_facade,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)


class CommunicationEventBridge:

    def publish_event(
        self,
        source: str,
        event_type: str,
        data: dict[str, Any] | None = None,
    ):
        return communication_facade.publish(
            topic=communication_topics.SYSTEM_EVENT,
            source=source,
            payload={
                "event_type": event_type,
                "data": dict(
                    data or {}
                ),
            },
        )


communication_event_bridge = (
    CommunicationEventBridge()
)
