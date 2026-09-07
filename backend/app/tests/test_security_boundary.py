from app.modules.security.security_boundary_service import (
    security_boundary_service,
)


def test_unknown_device_runtime_blocked():
    result = (
        security_boundary_service
        .check_runtime(
            device_id=(
                "unknown-device"
            )
        )
    )

    assert (
        result["allowed"]
        is False
    )


def test_unknown_device_module_blocked():
    result = (
        security_boundary_service
        .check_module(
            device_id=(
                "unknown-device"
            ),
            module="runtime",
        )
    )

    assert (
        result["allowed"]
        is False
    )
