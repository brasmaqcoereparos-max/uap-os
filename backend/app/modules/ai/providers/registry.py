"""
AI Provider Registry - Manage multiple providers
"""

import logging
from typing import Dict, Optional, List
from .base import AIProvider
from .mock import MockProvider
from ..schemas import ProviderHealth

logger = logging.getLogger(__name__)


class AIProviderRegistry:
    """
    Registry for managing AI providers
    Supports multiple providers with fallback mechanism
    """

    def __init__(self):
        self.providers: Dict[str, AIProvider] = {}
        self.default_provider: Optional[str] = None
        self._initialized = False

    async def register_provider(
        self,
        provider: AIProvider,
        default: bool = False
    ) -> bool:
        """Register an AI provider"""
        try:
            provider_name = provider.name
            logger.info(f"Registering provider: {provider_name}")

            # Initialize provider
            if not await provider.initialize():
                logger.warning(f"Provider {provider_name} failed initialization")
                self.providers[provider_name] = provider
                return False

            self.providers[provider_name] = provider

            if default or not self.default_provider:
                self.default_provider = provider_name
                logger.info(f"Set default provider: {provider_name}")

            logger.info(f"Provider {provider_name} registered successfully")
            return True

        except Exception as e:
            logger.error(f"Error registering provider: {e}")
            return False

    def get_provider(self, name: Optional[str] = None) -> Optional[AIProvider]:
        """Get provider by name or default"""
        if not name:
            name = self.default_provider

        if not name:
            return None

        return self.providers.get(name)

    def list_providers(self) -> List[str]:
        """List all registered providers"""
        return list(self.providers.keys())

    def has_provider(self, name: str) -> bool:
        """Check if provider is registered"""
        return name in self.providers

    async def get_health_all(self) -> Dict[str, ProviderHealth]:
        """Get health of all providers"""
        health = {}
        for name, provider in self.providers.items():
            try:
                health[name] = await provider.health_check()
            except Exception as e:
                logger.error(f"Health check failed for {name}: {e}")
                health[name] = provider.get_health()

        return health

    async def get_health(self, name: Optional[str] = None) -> Optional[ProviderHealth]:
        """Get health of specific provider"""
        provider = self.get_provider(name)
        if not provider:
            return None

        try:
            return await provider.health_check()
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return provider.get_health()

    async def initialize_default(self) -> bool:
        """Initialize with default mock provider"""
        try:
            mock_provider = MockProvider(name="mock")
            return await self.register_provider(mock_provider, default=True)
        except Exception as e:
            logger.error(f"Failed to initialize default provider: {e}")
            return False

    async def shutdown_all(self):
        """Shutdown all providers"""
        for provider in self.providers.values():
            try:
                await provider.shutdown()
            except Exception as e:
                logger.error(f"Error shutting down provider: {e}")

        self.providers.clear()
        self.default_provider = None


# Global registry instance
provider_registry = AIProviderRegistry()
