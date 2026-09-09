from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)


def test_component_identity_position_rotation_and_serialization():
    component = Component(
        component_id="motor-1",
        name="Motor",
        component_type="actuator",
        x=10,
        y=20,
        rotation=450,
        metadata={
            "width": 120,
            "height": 70,
            "z_index": 3,
        },
    )

    assert component.id == "motor-1"
    assert component.component_id == "motor-1"
    assert component.type == "actuator"

    assert component.position() == (
        10.0,
        20.0,
    )

    assert component.rotation == 90.0

    component.move_by(
        5,
        -10,
    )

    component.rotate(45)

    data = component.to_dict()

    assert data["id"] == "motor-1"
    assert data["type"] == "actuator"
    assert data["x"] == 15.0
    assert data["y"] == 10.0
    assert data["rotation"] == 135.0
    assert data["width"] == 120.0
    assert data["height"] == 70.0
    assert data["z_index"] == 3
