from app.modules.simulator.programming.simulator.device.device_registry import (
    DeviceRegistry,
)


class DummyDevice:

    def __init__(
        self,
        name,
    ):
        self.name = name


def test_device_registry_register_lookup_remove_and_clear():
    registry = DeviceRegistry()

    device = DummyDevice(
        "sensor-1"
    )

    assert registry.register(
        device
    ) is device

    assert registry.exists(
        "sensor-1"
    ) is True

    assert registry.get(
        "sensor-1"
    ) is device

    assert registry.names() == [
        "sensor-1"
    ]

    assert registry.values() == [
        device
    ]

    assert registry.count() == 1

    assert registry.unregister(
        "sensor-1"
    ) is device

    assert registry.count() == 0

    registry.register(
        "manual-name",
        device,
    )

    assert registry.clear() == 1
    assert registry.count() == 0
