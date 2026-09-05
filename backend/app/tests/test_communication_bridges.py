from app.modules.communication.ai_bridge import (
    communication_ai_bridge,
)
from app.modules.communication.automation_bridge import (
    communication_automation_bridge,
)
from app.modules.communication.device_bridge import (
    communication_device_bridge,
)
from app.modules.communication.event_bridge import (
    communication_event_bridge,
)
from app.modules.communication.runtime_bridge import (
    communication_runtime_bridge,
)
from app.modules.communication.ui_bridge import (
    communication_ui_bridge,
)
from app.modules.communication.voice_bridge import (
    communication_voice_bridge,
)


def test_event_bridge():
    result = (
        communication_event_bridge
        .publish_event(
            source="test",
            event_type="ping",
            data={
                "value": 1,
            },
        )
    )

    assert result is not None


def test_runtime_bridge():
    result = (
        communication_runtime_bridge
        .publish_runtime_event(
            source="test",
            event="ready",
        )
    )

    assert result is not None


def test_device_bridge_proposal():
    result = (
        communication_device_bridge
        .propose_device_command(
            device_id="device-1",
            command="start",
        )
    )

    assert (
        result[
            "requires_validation"
        ]
        is True
    )


def test_automation_bridge():
    result = (
        communication_automation_bridge
        .publish(
            automation_id="auto-1",
            event="started",
        )
    )

    assert result is not None


def test_ui_bridge():
    assert (
        communication_ui_bridge
        .publish(
            "refresh"
        )
        is not None
    )


def test_voice_bridge():
    assert (
        communication_voice_bridge
        .publish(
            "command"
        )
        is not None
    )


def test_ai_bridge():
    assert (
        communication_ai_bridge
        .publish(
            "proposal"
        )
        is not None
  )
