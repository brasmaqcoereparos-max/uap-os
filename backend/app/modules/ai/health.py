from app.modules.ai.openai_health import (
    openai_health,
)
from app.modules.ai.provider_manager import (
    ai_provider_manager,
)


class AIHealth:

    def check(self):
        providers = (
            ai_provider_manager
            .providers()
        )

        return {
            "healthy": True,
            "service": "ai",
            "providers": providers,
            "openai": (
                openai_health.check()
            ),
        }


ai_health = AIHealth()
