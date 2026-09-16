import pytest

from app.modules.runtime.runtime_context import (
    RuntimeContext,
)


def test_runtime_starts_when_safe():
    context = RuntimeContext(
        "project-safe"
    )

    context.start()

    assert context.state.running is True
    assert context.is_safe() is True


def test_interlock_blocks_runtime_start():
    context = RuntimeContext(
        "project-interlock"
    )

    context.interlocks.register(
        interlock_id="door",
        name="Safety door",
        condition=lambda: True,
    )

    with pytest.raises(
        RuntimeError
    ):
        context.start()

    assert (
        context.state.running
        is False
    )

    assert (
        context.state.emergency_stop
        is True
    )

    assert context.is_safe() is False


def test_emergency_stop_requires_reset():
    context = RuntimeContext(
        "project-estop"
    )

    context.start()
    context.emergency_stop(
        "Operator emergency stop"
    )

    assert (
        context.state.emergency_stop
        is True
    )

    assert (
        context.state.running
        is False
    )

    with pytest.raises(
        RuntimeError
    ):
        context.start()

    context.reset_emergency_stop()

    assert (
        context.state.emergency_stop
        is False
    )

    context.start()

    assert (
        context.state.running
        is True
    )


def test_active_interlock_blocks_estop_reset():
    context = RuntimeContext(
        "project-reset"
    )

    unsafe = {
        "active": False,
    }

    context.interlocks.register(
        interlock_id="guard",
        name="Machine guard",
        condition=lambda: unsafe[
            "active"
        ],
    )

    context.start()

    context.emergency_stop()

    unsafe["active"] = True

    with pytest.raises(
        RuntimeError
    ):
        context.reset_emergency_stop()

    assert (
        context.state.emergency_stop
        is True
    )

    unsafe["active"] = False

    context.reset_emergency_stop()

    assert (
        context.state.emergency_stop
        is False
    )


def test_interlock_status():
    context = RuntimeContext(
        "project-status"
    )

    context.interlocks.register(
        interlock_id="door",
        name="Door",
        condition=lambda: False,
    )

    status = context.status()

    assert (
        status["safe"]
        is True
    )

    assert (
        status["interlocks"][
            "registered"
        ]
        == 1
    )

    assert (
        status["interlocks"][
            "triggered"
        ]
        == []
  )
