import pytest

from app.modules.runtime.runtime_context import RuntimeContext


class FakeHardware:
    def __init__(self):
        self.writes = []

    def write(self, pin, value):
        self.writes.append(
            (pin, value)
        )
        return True

    def read(self, pin):
        return None

    def pwm(self, pin, duty):
        return True


def test_interlock_prevents_runtime_start():
    hardware = FakeHardware()

    context = RuntimeContext(
        "project-safe-hardware",
        hardware=hardware,
    )

    context.interlocks.register(
        interlock_id="guard",
        name="Machine guard",
        condition=lambda: True,
    )

    with pytest.raises(RuntimeError):
        context.start()

    assert context.state.running is False
    assert context.state.emergency_stop is True


def test_estop_cannot_reset_with_active_interlock():
    context = RuntimeContext(
        "project-reset-boundary"
    )

    unsafe = {
        "active": False,
    }

    context.interlocks.register(
        interlock_id="door",
        name="Door",
        condition=lambda: unsafe["active"],
    )

    context.start()
    context.emergency_stop()

    unsafe["active"] = True

    with pytest.raises(RuntimeError):
        context.reset_emergency_stop()

    assert context.state.emergency_stop is True


def test_estop_can_reset_after_safe_condition():
    context = RuntimeContext(
        "project-safe-reset"
    )

    unsafe = {
        "active": False,
    }

    context.interlocks.register(
        interlock_id="door",
        name="Door",
        condition=lambda: unsafe["active"],
    )

    context.start()
    context.emergency_stop()

    unsafe["active"] = False

    context.reset_emergency_stop()

    assert context.state.emergency_stop is False
    assert context.is_safe() is True
