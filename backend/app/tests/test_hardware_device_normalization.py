from app.modules.uhal.hardware_abstraction import (
    DeviceState,
    DeviceType,
    HardwareAbstractionLayer,
    HardwareDevice,
)


def test_hardware_device_normalizes_type_and_state():
    device = HardwareDevice(
        device_id="sensor-1",
        name="Sensor",
        device_type="sensor",
        state="online",
    )

    assert (
        device.device_type
        is DeviceType.SENSOR
    )

    assert (
        device.state
        is DeviceState.ONLINE
    )

    assert (
        device.to_dict()[
            "device_type"
        ]
        == "sensor"
    )

    hal = (
        HardwareAbstractionLayer()
    )

    hal.register_device(
        device
    )

    hal.set_device_state(
        "sensor-1",
        "error",
    )

    assert (
        device.state
        is DeviceState.ERROR
    )
