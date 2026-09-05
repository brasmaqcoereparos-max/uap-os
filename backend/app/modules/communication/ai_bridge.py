from typing import Any

from app.modules.communication.communication_facade import (
    communication_facade,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)


class CommunicationAIBridge:

    def publish(
        self,
        event: str,
        data: dict[str, Any] | None = None,
    ):
        return communication_facade.publish(
            topic=communication_topics.AI_EVENT,
            source="ai",
            payload={
                "event": event,
                "data": dict(
                    data or {}
                ),
            },
        )


communication_ai_bridge = (
    CommunicationAIBridge()
)
