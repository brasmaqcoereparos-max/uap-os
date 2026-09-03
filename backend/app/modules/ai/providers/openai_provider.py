import os

from app.modules.ai.providers.base import (
    AIProvider,
)
from app.modules.ai.schemas import (
    AIRequest,
    AIResponse,
)


class OpenAIProvider(
    AIProvider
):

    @property
    def name(self):
        return "openai"

    def available(self):
        return bool(
            os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def _client(self):
        if not self.available():
            raise RuntimeError(
                "OPENAI_API_KEY "
                "is not configured"
            )

        try:
            from openai import OpenAI

        except ImportError as exc:
            raise RuntimeError(
                "OpenAI Python SDK "
                "is not installed"
            ) from exc

        return OpenAI()

    def generate(
        self,
        request: AIRequest,
    ):
        if not self.available():
            return AIResponse(
                text="",
                provider=self.name,
                model=request.model,
                success=False,
                error=(
                    "OpenAI provider "
                    "is unavailable"
                ),
            )

        client = self._client()

        model = (
            request.model
            or os.getenv(
                "OPENAI_MODEL",
                "gpt-5.5",
            )
        )

        instructions = []
        inputs = []

        for message in request.messages:
            role = (
                message.role.value
                if hasattr(
                    message.role,
                    "value",
                )
                else str(
                    message.role
                )
            )

            if role == "system":
                instructions.append(
                    message.content
                )

            else:
                inputs.append(
                    {
                        "role": role,
                        "content": (
                            message.content
                        ),
                    }
                )

        kwargs = {
            "model": model,
            "input": inputs,
        }

        if instructions:
            kwargs[
                "instructions"
            ] = "\n\n".join(
                instructions
            )

        max_tokens = getattr(
            request,
            "max_output_tokens",
            None,
        )

        if max_tokens:
            kwargs[
                "max_output_tokens"
            ] = max_tokens

        try:
            response = (
                client.responses.create(
                    **kwargs
                )
            )

            usage = {}

            response_usage = getattr(
                response,
                "usage",
                None,
            )

            if response_usage:
                usage = {
                    "input_tokens": getattr(
                        response_usage,
                        "input_tokens",
                        None,
                    ),
                    "output_tokens": getattr(
                        response_usage,
                        "output_tokens",
                        None,
                    ),
                    "total_tokens": getattr(
                        response_usage,
                        "total_tokens",
                        None,
                    ),
                }

            return AIResponse(
                text=(
                    response.output_text
                    or ""
                ),
                provider=self.name,
                model=model,
                success=True,
                usage=usage,
                metadata={
                    "response_id": getattr(
                        response,
                        "id",
                        None,
                    ),
                },
            )

        except Exception as exc:
            return AIResponse(
                text="",
                provider=self.name,
                model=model,
                success=False,
                error=str(exc),
            )


openai_provider = (
    OpenAIProvider()
          )
