from app.modules.security.runtime_guard_result import (
    RuntimeGuardResult,
)


class TamperRuntimeGuard:

    def check(
        self,
        tamper_result: dict | None,
    ):
        if not tamper_result:
            return RuntimeGuardResult(
                allowed=True,
                status="allowed",
            )

        if tamper_result.get(
            "tampered",
            False,
        ):
            return RuntimeGuardResult(
                allowed=False,
                status=(
                    "tamper_detected"
                ),
                reasons=[
                    (
                        "File integrity "
                        "verification failed"
                    )
                ],
            )

        return RuntimeGuardResult(
            allowed=True,
            status="allowed",
        )


tamper_runtime_guard = (
    TamperRuntimeGuard()
)
