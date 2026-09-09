import pytest

from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)


def test_component_properties_and_metadata_are_mutable_and_serialized():
    component = Component(
        metadata={
            "icon": "motor.svg"
        }
    )

    component.set_property(
        "speed",
        1200,
    )

    component.update_properties(
        {
            "direction": "cw",
            "enabled": True,
        }
    )

    component.set_metadata(
        "category",
        "motion",
    )

    assert component.get_property("speed") == 1200
    assert component.get_property("direction") == "cw"
    assert component.get_metadata("icon") == "motor.svg"
    assert component.get_metadata("category") == "motion"

    data = component.to_dict()

    assert data["properties"]["enabled"] is True
    assert data["metadata"]["category"] == "motion"

    with pytest.raises(TypeError):
        component.update_properties(
            [
                (
                    "speed",
                    100,
                )
            ]
  )
