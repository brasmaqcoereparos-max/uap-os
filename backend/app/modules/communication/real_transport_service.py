from typing import Any

from app.modules.communication.provider_manager import (
    communication_provider_manager,
)


class CommunicationRealTransportService:

    def send(
        self,
        provider_name: str,
        destination: str,
        payload: dict[str, Any],
    ):
        provider = (
            communication_provider_manager
            .get(
                provider_name
            )
        )

        if not provider.available():
            return {
                "success": False,
                "provider": (
                    provider_name
                ),
                "error": (
                    "Provider unavailable"
                ),
            }

        result = provider.send(
            destination=destination,
            payload=payload,
        )

        return result.to_dict()


communication_real_transport_service = (
    CommunicationRealTransportService()
)
