from app.modules.communication.integration_status import (
    communication_integration_status,
)
from app.modules.communication.observability_service import (
    communication_observability_service,
)
from app.modules.communication.provider_health_service import (
    communication_provider_health_service,
)
from app.modules.communication.status import (
    communication_status,
)


class CommunicationFinalStatus:

    def snapshot(self):
        return {
            "communication": (
                communication_status
                .snapshot()
            ),
            "integration": (
                communication_integration_status
                .snapshot()
            ),
            "providers": (
                communication_provider_health_service
                .check()
            ),
            "observability": (
                communication_observability_service
                .snapshot()
            ),
            "block": {
                "name": (
                    "communication"
                ),
                "ready": True,
            },
        }


communication_final_status = (
    CommunicationFinalStatus()
)
