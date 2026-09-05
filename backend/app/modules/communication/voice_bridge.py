from typing import Any

from app.modules.communication.communication_facade import (
    communication_facade,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)


class CommunicationVoiceBridge:

    def publish(
        self,
        event: str,
        data: dict[str, Any] | None = None,
    ):
        return communication_facade.publish(
            topic=communication_topics.VOICE_EVENT,
            source="voice",
            payload={
                "event": event,
                "data": dict(
                    data or {}
                ),
            },
        )


communication_voice_bridge = (
    CommunicationVoiceBridge()
)
