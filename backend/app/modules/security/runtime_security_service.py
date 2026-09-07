from app.modules.security.license_runtime_guard import (
    license_runtime_guard,
)
from app.modules.security.runtime_guard_result import (
    RuntimeGuardResult,
)
from app.modules.security.runtime_security_policy import (
    runtime_security_policy,
)
from app.modules.security.security_auditor import (
    security_auditor,
)
from app.modules.security.tamper_runtime_guard import (
    tamper_runtime_guard,
)


class RuntimeSecurityService:

    def authorize(
        self,
        device_id: str,
        tamper_result: (
            dict | None
        ) = None,
    ):
        reasons = []

        if (
            runtime_security_policy
            .require_valid_license
        ):
            license_result = (
                license_runtime_guard
                .check(
                    device_id
                )
            )

            if not license_result.allowed:
                reasons.extend(
                    license_result.reasons
                )

        if (
            runtime_security_policy
            .block_on_tamper
        ):
            tamper_guard = (
                tamper_runtime_guard
                .check(
                    tamper_result
                )
            )

            if not tamper_guard.allowed:
                reasons.extend(
                    tamper_guard.reasons
                )

        allowed = not reasons

        result = RuntimeGuardResult(
            allowed=allowed,
            status=(
                "allowed"
                if allowed
                else "blocked"
            ),
            reasons=reasons,
        )

        if (
            not allowed
            and runtime_security_policy
            .audit_denials
        ):
            security_auditor.record(
                action=(
                    "runtime_authorization"
                ),
                success=False,
                target=device_id,
                details=(
                    result.to_dict()
                ),
            )

        elif (
            allowed
            and runtime_security_policy
            .audit_success
        ):
            security_auditor.record(
                action=(
                    "runtime_authorization"
                ),
                success=True,
                target=device_id,
                details=(
                    result.to_dict()
                ),
            )

        return result


runtime_security_service = (
    RuntimeSecurityService()
            )
