from datetime import datetime
from datetime import timezone

from app.modules.security.license_record import (
    LicenseRecord,
)
from app.modules.security.license_state import (
    LicenseState,
)
from app.modules.security.license_validation import (
    LicenseValidation,
)


class LicenseValidator:

    def validate(
        self,
        license_record: (
            LicenseRecord | None
        ),
        device_id: str,
    ):
        result = LicenseValidation(
            valid=True
        )

        if license_record is None:
            return result.add_error(
                "License not found"
            )

        if (
            license_record.device_id
            != device_id
        ):
            result.add_error(
                "License device mismatch"
            )

        if (
            license_record.state
            != LicenseState.ACTIVE
        ):
            result.add_error(
                "License is not active"
            )

        if (
            license_record.expires_at
            is not None
        ):
            now = datetime.now(
                timezone.utc
            )

            expires_at = (
                license_record
                .expires_at
            )

            if (
                expires_at.tzinfo
                is None
            ):
                expires_at = (
                    expires_at.replace(
                        tzinfo=timezone.utc
                    )
                )

            if now >= expires_at:
                result.add_error(
                    "License expired"
                )

        return result


license_validator = (
    LicenseValidator()
)
