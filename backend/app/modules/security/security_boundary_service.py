from app.modules.security.module_access_service import (
    security_module_access_service,
)
from app.modules.security.runtime_security_service import (
    runtime_security_service,
)


class SecurityBoundaryService:

    def check_module(
        self,
        device_id: str,
        module: str,
    ):
        return (
            security_module_access_service
            .check(
                device_id=device_id,
                module=module,
            )
        )

    def check_runtime(
        self,
        device_id: str,
        tamper_result: (
            dict | None
        ) = None,
    ):
        result = (
            runtime_security_service
            .authorize(
                device_id=device_id,
                tamper_result=(
                    tamper_result
                ),
            )
        )

        return result.to_dict()


security_boundary_service = (
    SecurityBoundaryService()
)
