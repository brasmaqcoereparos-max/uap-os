from app.modules.security.identity_service import (
    device_identity_service,
)


def test_device_identity_generation():
    identity = (
        device_identity_service
        .generate(
            serial_number=(
                "TEST-SERIAL"
            ),
            board="test-board",
            model="test-model",
        )
    )

    assert identity.device_id

    assert (
        identity.serial_number
        == "TEST-SERIAL"
    )

    assert identity.hardware_id

    assert (
        identity.board
        == "test-board"
    )
