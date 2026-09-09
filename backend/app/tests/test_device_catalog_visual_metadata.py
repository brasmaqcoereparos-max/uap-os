from app.modules.simulator.programming.simulator.device.device_catalog import (
    DeviceCatalog,
)


class DummyDevice:
    pass


def test_device_catalog_preserves_visual_and_custom_metadata():
    catalog = DeviceCatalog()

    catalog.register(
        "pump",
        DummyDevice,
        category="actuators",
        description="Pump",
        icon="pump.png",
        metadata={
            "image": "pump-large.png",
            "family": "fluid",
        },
    )

    info = catalog.info(
        "pump"
    )

    assert (
        info["icon"]
        == "pump.png"
    )

    assert (
        info[
            "metadata"
        ][
            "image"
        ]
        == "pump-large.png"
    )

    assert (
        info[
            "metadata"
        ][
            "family"
        ]
        == "fluid"
    )

    exported = catalog.metadata()

    assert (
        exported[
            "PUMP"
        ][
            "category"
        ]
        == "actuators"
    )
