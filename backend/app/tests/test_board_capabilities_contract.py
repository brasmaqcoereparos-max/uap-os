from app.modules.uhal.board_capabilities import (
    BoardCapabilities,
)


def test_board_capabilities_support_lookup_and_serialization():

    capabilities = (
        BoardCapabilities()
    )

    capabilities.gpio = 20

    capabilities.pwm = 6

    capabilities.wifi = True

    assert (
        capabilities.get(
            "GPIO"
        )
        == 20
    )

    assert (
        capabilities.supports(
            "gpio"
        )
        is True
    )

    assert (
        capabilities.supports(
            "pwm"
        )
        is True
    )

    assert (
        capabilities.supports(
            "wifi"
        )
        is True
    )

    assert (
        capabilities.supports(
            "camera"
        )
        is False
    )

    assert (
        capabilities.supports(
            "unknown"
        )
        is False
    )

    data = (
        capabilities.to_dict()
    )

    assert (
        data["gpio"]
        == 20
    )

    assert (
        data["wifi"]
        is True
    )

    assert (
        "gpio"
        in capabilities.available()
  )
