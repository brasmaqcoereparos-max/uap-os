from app.modules.security.protection_status import (
    security_protection_status,
)
from app.modules.security.security_health_service import (
    security_health_service,
)
from app.modules.security.security_status import (
    security_status,
)


class SecurityFinalStatus:

    def snapshot(self):
        return {
            "security": (
                security_status.snapshot()
            ),
            "health": (
                security_health_service.check()
            ),
            "protection": (
                security_protection_status
                .snapshot()
            ),
            "block": {
                "name": "security",
                "ready": True,
            },
        }


security_final_status = (
    SecurityFinalStatus()
)
