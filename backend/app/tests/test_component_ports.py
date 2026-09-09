from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)


def test_component_ports_preserve_type_direction_and_metadata():
    component = Component(
        name="Sensor"
    )

    port = component.add_port(
        "signal",
        port_type="gpio",
        direction="output",
        metadata={
            "voltage": 3.3,
            "required": True,
        },
    )

    assert component.has_port("signal") is True
    assert port["name"] == "signal"
    assert port["type"] == "gpio"
    assert port["direction"] == "output"
    assert port["metadata"]["voltage"] == 3.3
    assert port["metadata"]["required"] is True

    serialized = component.to_dict()

    assert (
        serialized["ports"]["signal"]
        == port
    )

    removed = component.remove_port(
        "signal"
    )

    assert removed == port
    assert component.has_port("signal") is False
