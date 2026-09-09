from app.modules.uhal.device_model import (
    UniversalDevice,
)


def test_universal_device_capabilities_connections_and_serialization():
    device = UniversalDevice(
        device_id="dev1",
        name="Board",
        device_type="controller",
        metadata={
            "icon": "board.svg",
        },
    )

    device.add_capability(
        "gpio",
        {
            "pins": 20,
        },
    )

    device.add_connection(
        "usb",
        address="local",
        parameters={
            "speed": "high",
        },
    )

    assert (
        device.has_capability(
            "gpio"
        )
        is True
    )

    data = device.to_dict()

    assert (
        data[
            "capabilities"
        ][
            0
        ][
            "parameters"
        ][
            "pins"
        ]
        == 20
    )

    assert (
        data[
            "connections"
        ][
            0
        ][
            "protocol"
        ]
        == "usb"
    )

    assert (
        data[
            "metadata"
        ][
            "icon"
        ]
        == "board.svg"
  )
