from datetime import datetime
from datetime import timedelta
from datetime import timezone

from app.modules.security.license_payload import (
    LicensePayload,
)
from app.modules.security.license_signature_verifier import (
    license_signature_verifier,
)
from app.modules.security.license_signer import (
    license_signer,
)


def test_license_signature():
    payload = LicensePayload(
        license_id="license-test",
        device_id="device-test",
        issued_at=datetime.now(
            timezone.utc
        ),
        expires_at=(
            datetime.now(
                timezone.utc
            )
            + timedelta(
                days=30
            )
        ),
        features=[
            "runtime",
            "simulator",
        ],
    )

    signed = license_signer.sign(
        payload=payload,
        secret="test-secret",
    )

    result = (
        license_signature_verifier
        .verify(
            signed_license=signed,
            secret="test-secret",
        )
    )

    assert result[
        "valid"
    ] is True


def test_invalid_secret_rejected():
    payload = LicensePayload(
        license_id="license-test",
        device_id="device-test",
    )

    signed = license_signer.sign(
        payload=payload,
        secret="correct-secret",
    )

    result = (
        license_signature_verifier
        .verify(
            signed_license=signed,
            secret="wrong-secret",
        )
    )

    assert result[
        "valid"
    ] is False
