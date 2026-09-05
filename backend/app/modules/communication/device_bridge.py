from typing import Any

from app.modules.communication.communication_facade import (
    communication_facade,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)


class CommunicationDeviceBridge:

    def publish_device_event(
        self,
        device_id: str,
        event: str,
        data: dict[str, Any] | None = None,
    ):
        return communication_facade.publish(
            topic=communication_topics.DEVICE_EVENT,
            source=f"device:{device_id}",
            payload={
                "device_id": device_id,
                "event": event,
                "data": dict(
                    data or {}
                ),
            },
        )

    def propose_device_command(
        self,
        device_id: str,
        command: str,
        parameters: dict[str, Any] | None = None,
    ):
        return {
            "topic": (
                communication_topics
                .DEVICE_COMMAND
            ),
            "source": "communication",
            "target": device_id,
            "payload": {
                "command": command,
                "parameters": dict(
                    parameters or {}
                ),
            },
            "requires_validation": True,
        }


communication_device_bridge = (
    CommunicationDeviceBridge()
    )
