from app.modules.communication.provider_health import (
    CommunicationProviderHealth,
)
from app.modules.communication.provider_manager import (
    communication_provider_manager,
)


class CommunicationProviderHealthService:

    def check(self):
        providers = (
            communication_provider_manager
            .providers()
        )

        return [
            CommunicationProviderHealth(
                name=item["name"],
                available=(
                    item["available"]
                ),
                state=(
                    "available"
                    if item[
                        "available"
                    ]
                    else "unavailable"
                ),
                details={},
            ).to_dict()
            for item in providers
        ]


communication_provider_health_service = (
    CommunicationProviderHealthService()
)
