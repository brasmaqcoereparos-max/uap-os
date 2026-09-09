from app.modules.simulator.health import (
    simulator_health,
)
from app.modules.simulator.status import (
    simulator_status,
)


def test_simulator_health():
    result = (
        simulator_health
        .check()
    )

    assert (
        result["service"]
        == "simulator"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["available"]
        is True
    )


def test_simulator_status():
    result = (
        simulator_status
        .snapshot()
    )

    assert (
        result["service"]
        == "simulator"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["components"][
            "programming"
        ]
        is True
    )

    assert (
        result["components"][
            "canvas"
        ]
        is True
    )

    assert (
        result["components"][
            "codegen"
        ]
        is True
    )
