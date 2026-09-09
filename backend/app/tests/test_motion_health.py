from app.modules.motion.health import (
    motion_health,
)
from app.modules.motion.status import (
    motion_status,
)


def test_motion_health():
    result = (
        motion_health
        .check()
    )

    assert (
        result["service"]
        == "motion"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["available"]
        is True
    )


def test_motion_status():
    result = (
        motion_status
        .snapshot()
    )

    assert (
        result["service"]
        == "motion"
    )

    assert (
        result["components"][
            "motion_manager"
        ]
        is True
    )

    assert (
        result["components"][
            "trajectory"
        ]
        is True
    )

    assert (
        result["components"][
            "teach_mode"
        ]
        is True
    )
