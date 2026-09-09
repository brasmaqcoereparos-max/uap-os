from app.modules.uhal.compatibility import (
    HardwareCompatibilityChecker,
)

from app.modules.uhal.device_model import (
    UniversalDevice,
)


def test_component_requirements_can_be_checked_against_device_capabilities():
    device = UniversalDevice(
        device_id="esp",
        name="ESP",
        device_type="board",
    )

    device.add_capability(
        "gpio"
    )

    device.add_capability(
        "pwm"
    )

    checker = (
        HardwareCompatibilityChecker()
    )

    result = checker.check(
        device,
        [
            "gpio",
            "pwm",
        ],
    )

    assert result.compatible is True

    assert (
        result.missing_capabilities
        == []
    )

    incompatible = checker.check(
        device,
        [
            "gpio",
            "adc",
        ],
    )

    assert (
        incompatible.compatible
        is False
    )

    assert (
        incompatible.missing_capabilities
        == [
            "adc"
        ]
  )
