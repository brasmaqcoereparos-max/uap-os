from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_manager import (
    ComponentManager,
)


class DummyDevice:

    def __init__(self):
        self.name = "motor-device"
        self.update_calls = 0
        self.enabled = True

    def update(self):
        self.update_calls += 1

        return {
            "updated": self.update_calls
        }

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def to_dict(self):
        return {
            "name": self.name,
            "enabled": self.enabled,
        }


def test_component_device_simulator_boundary():
    manager = ComponentManager()

    component = Component(
        component_id="motor-1",
        name="Motor",
        component_type="motor",
    )

    device = DummyDevice()

    manager.add(component)

    assert manager.bind_device(
        "motor-1",
        device,
    ) is True

    assert component.has_device() is True

    updates = manager.update_devices()

    assert updates["motor-1"] == {
        "updated": 1
    }

    component.disable()

    assert device.enabled is False

    component.enable()

    assert device.enabled is True

    data = component.to_dict()

    assert data["device"]["name"] == "motor-device"
    assert data["device"]["enabled"] is True
