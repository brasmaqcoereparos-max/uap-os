from app.modules.security.security_status import (
    security_status,
)


class SecurityHealthService:

    def check(self):
        status = (
            security_status
            .snapshot()
        )

        return {
            "healthy": (
                status[
                    "healthy"
                ]
            ),
            "service": (
                status[
                    "service"
                ]
            ),
            "license_stored": (
                status[
                    "license"
                ][
                    "stored"
                ]
            ),
            "registered_licenses": (
                status[
                    "license"
                ][
                    "registered"
                ]
            ),
            "bindings": (
                status[
                    "bindings"
                ]
            ),
            "keys": (
                status[
                    "keys"
                ]
            ),
        }


security_health_service = (
    SecurityHealthService()
)
