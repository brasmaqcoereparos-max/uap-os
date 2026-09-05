from app.modules.communication.message_bus import (
    communication_message_bus,
)


def test_message_bus_publish():
    received = []

    def handler(message):
        received.append(
            message
        )

        return "ok"

    communication_message_bus
    .subscribe(
        topic="test.topic",
        subscriber_id=(
            "test-subscriber"
        ),
        handler=handler,
    )

    result = (
        communication_message_bus
        .publish(
            topic="test.topic",
            source="test",
            payload={
                "value": 1,
            },
        )
    )

    assert result.delivered is True

    assert len(received) == 1


def test_unknown_topic_not_delivered():
    result = (
        communication_message_bus
        .publish(
            topic=(
                "unknown.topic"
            ),
            source="test",
        )
    )

    assert (
        result.delivered
        is False
        )
