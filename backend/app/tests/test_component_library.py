from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_library import (
    ComponentLibrary,
)


def test_component_library_register_create_alias_and_metadata():
    library = ComponentLibrary()

    library.register(
        Component,
        name="MotorComponent",
        category="motion",
        description="Motor visual",
        icon="motor.svg",
        aliases=[
            "motor",
            "dc_motor",
        ],
        tags=[
            "actuator",
            "rotation",
        ],
        version="1.2",
    )

    assert library.exists("MotorComponent") is True
    assert library.exists("motor") is True
    assert library.get("dc_motor") is Component

    info = library.info("motor")

    assert info["category"] == "motion"
    assert info["icon"] == "motor.svg"
    assert info["version"] == "1.2"

    instance = library.create(
        "motor",
        name="M1",
        component_type="motor",
    )

    assert isinstance(
        instance,
        Component,
    )

    assert instance.name == "M1"
    assert instance.type == "motor"
