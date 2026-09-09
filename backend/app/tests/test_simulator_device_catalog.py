from app.modules.simulator.programming.simulator.device.device_catalog import (
    DeviceCatalog,
)


class DummyDevice:

    def __init__(
        self,
        name="dummy",
    ):
        self.name = name


def test_device_catalog_registration_metadata_categories_and_search():
    catalog = DeviceCatalog()

    catalog.register(
        "temperature_sensor",
        DummyDevice,
        category="sensors",
        description="Sensor de temperatura",
        icon="temperature.svg",
        metadata={
            "interface": "i2c"
        },
    )

    assert catalog.exists(
        "TEMPERATURE_SENSOR"
    ) is True

    assert catalog.get(
        "temperature_sensor"
    ) is DummyDevice

    assert catalog.categories() == [
        "sensors"
    ]

    assert catalog.by_category(
        "SENSORS"
    ) == {
        "TEMPERATURE_SENSOR": DummyDevice
    }

    assert catalog.search(
        "temperatura"
    ) == [
        "TEMPERATURE_SENSOR"
    ]

    info = catalog.info(
        "temperature_sensor"
    )

    assert info["icon"] == "temperature.svg"
    assert info["metadata"]["interface"] == "i2c"
