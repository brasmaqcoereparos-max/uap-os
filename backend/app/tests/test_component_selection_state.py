from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_manager import (
    ComponentManager,
)


def test_component_manager_exclusive_selection_and_state():
    manager = ComponentManager()

    first = Component(
        component_id="a"
    )

    second = Component(
        component_id="b"
    )

    manager.add(
        first
    )

    manager.add(
        second
    )

    manager.select(
        "a"
    )

    manager.select(
        "b",
        exclusive=True,
    )

    assert first.selected is False
    assert second.selected is True

    assert manager.selected() == [
        second
    ]

    second.disable()

    assert manager.enabled() == [
        first
    ]

    manager.clear_selection()

    assert manager.selected() == []
