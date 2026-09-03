from app.modules.ai.openai_config import (
    openai_config,
)
from app.modules.ai.providers.openai_provider import (
    openai_provider,
)


class OpenAIHealth:

    def check(self):
        sdk_available = True

        try:
            import openai  # noqa: F401

        except ImportError:
            sdk_available = False

        configured = (
            openai_config
            .api_key_configured
        )

        return {
            "provider": "openai",
            "enabled": (
                openai_config.enabled
            ),
            "configured": configured,
            "sdk_available": (
                sdk_available
            ),
            "available": (
                openai_config.enabled
                and sdk_available
                and openai_provider
                .available()
            ),
            "model": (
                openai_config.model
            ),
        }


openai_health = (
    OpenAIHealth()
)
