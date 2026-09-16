import pytest

from app.modules.runtime.interlock_manager import InterlockManager


def test_interlock_safe_condition():
    manager = InterlockManager()

    manager.register(
        interlock_id="door",
        name="Safety door",
        condition=lambda: False,
    )

    assert manager.is_safe() is True
    assert manager.check() == []


def test_interlock_detects_unsafe_condition():
    manager = InterlockManager()

    manager.register(
        interlock_id="guard",
        name="Machine guard",
        condition=lambda: True,
    )

    triggered = manager.check()

    assert manager.is_safe() is False
    assert len(triggered) == 1
    assert triggered[0].interlock_id == "guard"


def test_interlock_fails_safe_on_condition_error():
    manager = InterlockManager()

    def broken_condition():
        raise RuntimeError("sensor failure")

    manager.register(
        interlock_id="sensor",
        name="Safety sensor",
        condition=broken_condition,
    )

    triggered = manager.check()

    assert len(triggered) == 1
    assert triggered[0].interlock_id == "sensor"


def test_invalid_interlock_action_is_rejected():
    manager = InterlockManager()

    with pytest.raises(ValueError):
        manager.register(
            interlock_id="invalid",
            name="Invalid",
            condition=lambda: False,
            action="ignore",
        )
