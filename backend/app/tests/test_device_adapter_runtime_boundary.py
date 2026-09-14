from app.modules.uhal.device_adapter import (
    DeviceAdapter,
)

from app.modules.uhal.device_model import (
    UniversalDevice,
)

from app.modules.uhal.hardware_abstraction import (
    DeviceType,
    HardwareAbstractionLayer,
)


def test_device_adapter_preserves_runtime_device_contract():
    device = UniversalDevice(
        device_id="temperature-1",
        name="Temperature Sensor",
        device_type="sensor",
        metadata={
            "zone": "A",
        },
    )

    device.inputs[
        "temperature"
    ] = {
        "data_type": "float",
        "value": 23.5,
        "metadata": {
            "unit": "C",
        },
    }

    device.outputs[
        "alarm"
    ] = {
        "data_type": "bool",
        "value": False,
        "metadata": {
            "kind": "digital",
        },
    }

    device.add_capability(
        "sensor"
    )

    hal = (
        HardwareAbstractionLayer()
    )

    hardware = (
        DeviceAdapter(hal)
        .attach(device)
    )

    assert (
        hardware.device_type
        is DeviceType.SENSOR
    )

    assert (
        hardware.metadata
        == {
            "zone": "A",
        }
    )

    assert (
        hardware.get_input(
            "temperature"
        )
        == 23.5
    )

    assert (
        hardware.inputs[
            "temperature"
        ].metadata
        == {
            "unit": "C",
        }
    )

    assert (
        hardware.get_output(
            "alarm"
        )
        is False
    )

    assert (
        hardware.outputs[
            "alarm"
        ].metadata
        == {
            "kind": "digital",
        }
    )

    assert (
        hardware.to_dict()[
            "device_type"
        ]
        == "sensor"
  )
