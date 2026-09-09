from app.modules.uhal.hardware_registry import (
    HardwareRegistry,
)


class DummyDriver:
    pass


def test_hardware_registry_lifecycle():
    registry = (
        HardwareRegistry()
    )

    driver = (
        DummyDriver()
    )

    registry.register(
        "ESP32",
        driver,
    )

    assert registry.count() == 1

    assert registry.get(
        "esp32"
    ) is driver

    assert registry.get(
        "ESP32"
    ) is driver

    assert registry.names() == [
        "esp32"
    ]

    assert registry.all() == {
        "esp32": driver
    }

    removed = registry.unregister(
        "ESP32"
    )

    assert removed is driver

    assert registry.count() == 0
