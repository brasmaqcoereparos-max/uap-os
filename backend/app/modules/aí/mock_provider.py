from app.modules.ai.provider import (
    AIProvider,
)
from app.modules.ai.request import (
    AIRequest,
)
from app.modules.ai.response import (
    AIResponse,
)


class AIMockProvider(
    AIProvider
):

    @property
    def name(self):
        return "mock"

    def available(self):
        return True

    def generate(
        self,
        request: AIRequest,
    ):
        text = ""

        for message in reversed(
            request.messages
        ):
            if (
                message.role.value
                == "user"
            ):
                text = message.content
                break

        return AIResponse(
            text=(
                "UAP AI simulation: "
                f"{text}"
            ),
            provider=self.name,
            model="mock",
            success=True,
            metadata={
                "simulation": True,
            },
        )


ai_mock_provider = (
    AIMockProvider()
)
