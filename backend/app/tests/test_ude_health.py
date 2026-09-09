from app.modules.ude.health import (
    ude_health,
)
from app.modules.ude.status import (
    ude_status,
)


def test_ude_health():
    result = (
        ude_health
        .check()
    )

    assert isinstance(
        result,
        dict,
    )


def test_ude_status():
    result = (
        ude_status
        .snapshot()
    )

    assert (
        result["service"]
        == "ude"
    )

    assert (
        result["components"][
            "ude_manager"
        ]
        is True
    )

    assert (
        result["components"][
            "uhal_bridge"
        ]
        is True
    )
