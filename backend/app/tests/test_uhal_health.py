from app.modules.uhal.health import (
    uhal_health,
)
from app.modules.uhal.status import (
    uhal_status,
)


def test_uhal_health():
    result = (
        uhal_health
        .check()
    )

    assert (
        result["service"]
        == "uhal"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["available"]
        is True
    )


def test_uhal_status():
    result = (
        uhal_status
        .snapshot()
    )

    assert (
        result["service"]
        == "uhal"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["components"][
            "hal_manager"
        ]
        is True
    )
