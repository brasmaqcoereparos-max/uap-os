from app.modules.security.anti_copy_service import (
    anti_copy_service,
)
from app.modules.security.license_signature_verifier import (
    license_signature_verifier,
)
from app.modules.security.signed_license import (
    SignedLicense,
)


class LicenseIntegrityService:

    def validate(
        self,
        signed_license: SignedLicense,
        secret: str,
        device_id: str,
        hardware_id: str,
    ):
        signature = (
            license_signature_verifier
            .verify(
                signed_license=(
                    signed_license
                ),
                secret=secret,
            )
        )

        if not signature[
            "valid"
        ]:
            return {
                "valid": False,
                "signature": (
                    signature
                ),
                "binding": None,
            }

        license_id = str(
            signed_license
            .payload.get(
                "license_id",
                "",
            )
        )

        binding = (
            anti_copy_service
            .validate_binding(
                license_id=license_id,
                device_id=device_id,
                hardware_id=hardware_id,
            )
        )

        return {
            "valid": (
                signature["valid"]
                and binding["allowed"]
            ),
            "signature": (
                signature
            ),
            "binding": (
                binding
            ),
        }


license_integrity_service = (
    LicenseIntegrityService()
)
