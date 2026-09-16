import pytest

from app.modules.runtime.automation_state import AutomationState


def test_runtime_state_complete_cycle():
    state = AutomationState("project-final")

    state.start()

    assert state.running is True
    assert state.paused is False

    state.pause()

    assert state.running is True
    assert state.paused is True

    state.resume()

    assert state.running is True
    assert state.paused is False

    state.increment_cycle()

    assert state.cycle == 1

    state.stop()

    assert state.running is False
    assert state.paused is False


def test_emergency_stop_requires_explicit_reset():
    state = AutomationState("project-estop")

    state.start()
    state.emergency_stop_now()

    assert state.emergency_stop is True
    assert state.running is False

    with pytest.raises(RuntimeError):
        state.start()

    state.reset_emergency_stop()

    assert state.emergency_stop is False

    state.start()

    assert state.running is True


def test_runtime_state_serialization():
    state = AutomationState("project-serialization")

    state.set_value("temperature", 25)
    state.increment_cycle()

    data = state.to_dict()

    assert data["project_id"] == "project-serialization"
    assert data["cycle"] == 1
    assert data["values"]["temperature"] == 25
    assert data["updated_at"] is not None
