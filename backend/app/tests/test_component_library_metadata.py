from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_library import (
    ComponentLibrary,
)


def test_component_library_categories_tags_search_info_and_export():
    library = ComponentLibrary()

    library.register(
        Component,
        name="Motor",
        category="motion",
        description="DC motor",
        icon="motor.svg",
        aliases=[
            "dc",
        ],
        tags=[
            "actuator",
            "rotary",
        ],
        version="2.0",
    )

    assert library.categories() == [
        "motion"
    ]

    assert library.by_category(
        "MOTION"
    ) == [
        "Motor"
    ]

    assert library.by_tag(
        "ACTUATOR"
    ) == [
        "Motor"
    ]

    assert library.search(
        "rotary"
    ) == [
        "Motor"
    ]

    info = library.info(
        "dc"
    )

    assert info["icon"] == "motor.svg"
    assert info["version"] == "2.0"

    data = library.to_dict()

    assert data["count"] == 1

    assert (
        data[
            "components"
        ][
            "Motor"
        ][
            "version"
        ]
        == "2.0"
  )
