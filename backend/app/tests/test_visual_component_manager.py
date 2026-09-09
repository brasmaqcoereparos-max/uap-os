from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_manager import (
    ComponentManager,
)


def test_component_manager_manages_visual_component_lifecycle():
    manager = ComponentManager()

    component = Component(
        component_id="c1",
        name="Motor",
        component_type="motor",
    )

    assert manager.add(component) is component
    assert manager.exists("c1") is True
    assert manager.count() == 1

    assert manager.find_by_name(
        "motor"
    ) == [component]

    assert manager.find_by_type(
        "MOTOR"
    ) == [component]

    assert manager.move(
        "c1",
        30,
        40,
    ) is True

    assert component.position() == (
        30.0,
        40.0,
    )

    assert manager.select(
        "c1",
        exclusive=True,
    ) is True

    assert component.selected is True

    serialized = manager.to_dict()

    assert serialized["c1"]["id"] == "c1"

    assert manager.remove(
        "c1"
    ) is component

    assert manager.count() == 0
