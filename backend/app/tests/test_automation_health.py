from app.modules.automation.health import (
    automation_health,
)
from app.modules.automation.status import (
    automation_status,
)


def test_automation_health():
    result = (
        automation_health
        .check()
    )

    assert (
        result["service"]
        == "automation"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["available"]
        is True
    )


def test_automation_status():
    result = (
        automation_status
        .snapshot()
    )

    assert (
        result["service"]
        == "automation"
    )

    assert (
        result["healthy"]
        is True
    )
