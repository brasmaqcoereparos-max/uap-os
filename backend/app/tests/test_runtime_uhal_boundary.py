from app.modules.runtime.hardware_events import (
    HardwareEvent,
)

from app.modules.runtime.runtime_context import (
    RuntimeContext,
)


def test_runtime_context_io_state_and_event_boundary():
    context = RuntimeContext(
        "project-1"
    )

    received = []

    context.events.subscribe(
        "gpio.changed",
        received.append,
    )

    context.io.configure(
        "lamp",
        "output",
        "bool",
    )

    context.start()

    context.io.write(
        "lamp",
        True,
    )

    context.events.publish(
        HardwareEvent(
            event_type=(
                "gpio.changed"
            ),
            source="lamp",
            value=True,
        )
    )

    assert (
        context.state.running
        is True
    )

    assert (
        context.io.read(
            "lamp"
        )
        is True
    )

    assert len(
        received
    ) == 1

    assert (
        received[0].value
        is True
    )

    context.pause()

    assert (
        context.state.paused
        is True
    )

    context.resume()

    assert (
        context.state.paused
        is False
    )

    context.emergency_stop()

    assert (
        context.state.emergency_stop
        is True
    )

    assert (
        context.state.running
        is False
  )
