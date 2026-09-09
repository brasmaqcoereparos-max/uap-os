from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_library import (
    ComponentLibrary,
)


def test_component_library_unregister_removes_aliases_and_metadata():
    library = ComponentLibrary()

    library.register(
        Component,
        name="Sensor",
        aliases=[
            "sensor_alias",
        ],
    )

    assert (
        library.unregister(
            "sensor_alias"
        )
        is Component
    )

    assert (
        library.exists(
            "Sensor"
        )
        is False
    )

    assert (
        library.exists(
            "sensor_alias"
        )
        is False
    )

    assert (
        library.info(
            "Sensor"
        )
        is None
    )
