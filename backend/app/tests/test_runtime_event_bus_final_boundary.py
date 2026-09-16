from app.modules.runtime.hardware_events import (
    HardwareEvent,
    HardwareEventBus,
)


def test_event_bus_publish_subscribe():
    bus = HardwareEventBus()

    received = []

    bus.subscribe(
        "gpio.changed",
        received.append,
    )

    event = HardwareEvent(
        event_type="gpio.changed",
        source="GPIO18",
        value=True,
    )

    bus.publish(event)

    assert len(received) == 1
    assert received[0] is event
    assert received[0].value is True


def test_event_bus_unsubscribe():
    bus = HardwareEventBus()

    received = []

    def handler(event):
        received.append(event)

    bus.subscribe(
        "runtime.started",
        handler,
    )

    assert bus.unsubscribe(
        "runtime.started",
        handler,
    ) is True

    bus.publish(
        HardwareEvent(
            event_type="runtime.started"
        )
    )

    assert received == []


def test_event_bus_clear():
    bus = HardwareEventBus()

    received = []

    bus.subscribe(
        "runtime.stopped",
        received.append,
    )

    bus.clear()

    bus.publish(
        HardwareEvent(
            event_type="runtime.stopped"
        )
    )

    assert received == []
