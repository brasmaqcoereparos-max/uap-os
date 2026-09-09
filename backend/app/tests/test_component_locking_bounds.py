import pytest

from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)


def test_component_size_bounds_lock_and_hit_test():
    component = Component(
        component_id="c",
        x=10,
        y=20,
        metadata={
            "width": 50,
            "height": 30,
        },
    )

    assert component.bounds() == {
        "x": 10.0,
        "y": 20.0,
        "width": 50.0,
        "height": 30.0,
        "right": 60.0,
        "bottom": 50.0,
    }

    assert component.contains_point(
        20,
        30,
    ) is True

    assert component.contains_point(
        61,
        30,
    ) is False

    assert component.set_size(
        80,
        40,
    ) == (
        80.0,
        40.0,
    )

    component.lock()

    component.move_to(
        100,
        100,
    )

    assert component.position() == (
        10.0,
        20.0,
    )

    component.unlock()

    component.move_to(
        100,
        100,
    )

    assert component.position() == (
        100.0,
        100.0,
    )

    with pytest.raises(
        ValueError
    ):
        component.set_size(
            0,
            1,
        )
