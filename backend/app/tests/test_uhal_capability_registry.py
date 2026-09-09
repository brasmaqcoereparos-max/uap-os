from app.modules.uhal.capability_registry import (
    CapabilityRegistry,
    create_default_registry,
)


def test_default_hardware_capabilities_exist():
    registry = (
        create_default_registry()
    )

    required = [
        "gpio",
        "digital_read",
        "digital_write",
        "analog_read",
        "pwm",
        "servo",
        "i2c",
        "spi",
        "uart",
        "can",
        "wifi",
        "bluetooth",
        "camera",
        "display",
        "motor",
        "stepper",
        "relay",
        "sensor",
    ]

    for capability in required:
        assert registry.exists(
            capability
        ) is True


def test_custom_capability_registration():
    registry = (
        CapabilityRegistry()
    )

    registry.register(
        "laser",
        metadata={
            "type": "output",
            "safety_required": True,
        },
    )

    capability = registry.get(
        "LASER"
    )

    assert capability is not None

    assert capability[
        "name"
    ] == "laser"

    assert (
        capability[
            "metadata"
        ][
            "type"
        ]
        == "output"
    )

    assert (
        capability[
            "metadata"
        ][
            "safety_required"
        ]
        is True
    )
