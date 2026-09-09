from app.modules.simulator.programming.simulator.device.device_catalog import (
    device_catalog,
)

from app.modules.simulator.programming.simulator.device.device_factory import (
    DeviceFactory,
)


class DummyDevice:

    def __init__(
        self,
        name="dummy",
        pin=None,
    ):
        self.name = name
        self.pin = pin


def test_device_factory_creates_registered_device_from_definition():
    factory = DeviceFactory()

    device_catalog.clear()

    try:
        device_catalog.register(
            "dummy",
            DummyDevice,
            category="test",
        )

        device = factory.create_from_definition(
            {
                "type": "dummy",
                "name": "D1",
                "parameters": {
                    "pin": 17
                },
            }
        )

        assert isinstance(
            device,
            DummyDevice,
        )

        assert device.name == "D1"
        assert device.pin == 17

        assert factory.exists(
            "dummy"
        ) is True

        assert factory.count() == 1

    finally:
        device_catalog.clear()
