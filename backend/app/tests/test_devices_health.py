from app.modules.devices.health import (
    devices_health,
)
from app.modules.devices.status import (
    devices_status,
)


def test_devices_health():
    result = (
        devices_health
        .check()
    )

    assert (
        result["service"]
        == "devices"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["available"]
        is True
    )


def test_devices_status():
    result = (
        devices_status
        .snapshot()
    )

    assert (
        result["service"]
        == "devices"
    )

    assert (
        result["components"][
            "device_manager"
        ]
        is True
    )

    assert (
        result["components"][
            "gpio_device"
        ]
        is True
    )
