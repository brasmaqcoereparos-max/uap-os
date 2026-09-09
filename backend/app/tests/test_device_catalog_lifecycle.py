import pytest

from app.modules.simulator.programming.simulator.device.device_catalog import (
    DeviceCatalog,
)


class DeviceA:
    pass


class DeviceB:
    pass


def test_device_catalog_duplicate_unregister_and_clear():
    catalog = DeviceCatalog()

    catalog.register(
        "motor",
        DeviceA,
        replace=False,
    )

    with pytest.raises(
        ValueError
    ):
        catalog.register(
            "motor",
            DeviceB,
            replace=False,
        )

    assert (
        catalog.unregister(
            "motor"
        )
        is DeviceA
    )

    assert catalog.count() == 0

    catalog.register(
        "a",
        DeviceA,
    )

    catalog.register(
        "b",
        DeviceB,
    )

    assert catalog.count() == 2

    catalog.clear()

    assert catalog.count() == 0
