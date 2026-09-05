from app.modules.communication.provider_config import (
    CommunicationProviderConfig,
)
from app.modules.communication.provider_config_registry import (
    communication_provider_config_registry,
)


class CommunicationProviderConfigService:

    def set(
        self,
        name: str,
        enabled: bool = True,
        settings: dict | None = None,
    ):
        config = (
            CommunicationProviderConfig(
                name=name,
                enabled=enabled,
                settings=dict(
                    settings or {}
                ),
            )
        )

        return (
            communication_provider_config_registry
            .register(config)
        )

    def get(
        self,
        name: str,
    ):
        return (
            communication_provider_config_registry
            .get(name)
        )

    def list_all(self):
        return [
            config.to_dict()
            for config
            in communication_provider_config_registry
            .list_all()
        ]


communication_provider_config_service = (
    CommunicationProviderConfigService()
)
