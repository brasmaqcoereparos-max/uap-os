from app.modules.security.license_service import (
    license_service,
)
from app.modules.security.runtime_guard_result import (
    RuntimeGuardResult,
)


class LicenseRuntimeGuard:

    def check(
        self,
        device_id: str,
    ):
        result = (
            license_service
            .validate_device(
                device_id
            )
        )

        validation = result[
            "validation"
        ]

        if not validation[
            "valid"
        ]:
            return RuntimeGuardResult(
                allowed=False,
                status=(
                    "license_invalid"
                ),
                reasons=list(
                    validation.get(
                        "errors",
                        [],
                    )
                ),
            )

        return RuntimeGuardResult(
            allowed=True,
            status="allowed",
        )


license_runtime_guard = (
    LicenseRuntimeGuard()
)
