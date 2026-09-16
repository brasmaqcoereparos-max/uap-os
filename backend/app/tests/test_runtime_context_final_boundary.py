import pytest

from app.modules.runtime.runtime_context import RuntimeContext


def test_runtime_context_lifecycle():
    context = RuntimeContext(
        "project-context"
    )

    context.start()

    assert context.state.running is True

    context.pause()

    assert context.state.paused is True

    context.resume()

    assert context.state.paused is False

    context.stop()

    assert context.state.running is False


def test_runtime_context_interlock_blocks_start():
    context = RuntimeContext(
        "project-interlock"
    )

    context.interlocks.register(
        interlock_id="door",
        name="Door",
        condition=lambda: True,
    )

    with pytest.raises(RuntimeError):
        context.start()

    assert context.state.running is False
    assert context.state.emergency_stop is True


def test_runtime_context_estop_reset():
    context = RuntimeContext(
        "project-estop"
    )

    context.start()
    context.emergency_stop(
        "test"
    )

    assert context.state.emergency_stop is True

    context.reset_emergency_stop()

    assert context.state.emergency_stop is False


def test_runtime_context_status_contract():
    context = RuntimeContext(
        "project-status"
    )

    status = context.status()

    assert status["project_id"] == "project-status"
    assert "automation" in status
    assert "safe" in status
    assert "hardware_bound" in status
    assert "interlocks" in status
    assert "ports" in status
    assert "sensors" in status
    assert "actuators" in status
