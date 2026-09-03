import os
from dataclasses import dataclass


@dataclass
class OpenAIConfig:
    model: str = "gpt-5.5"

    enabled: bool = True

    @classmethod
    def from_environment(
        cls,
    ):
        return cls(
            model=os.getenv(
                "OPENAI_MODEL",
                "gpt-5.5",
            ),
            enabled=(
                os.getenv(
                    "OPENAI_ENABLED",
                    "true",
                )
                .strip()
                .lower()
                not in {
                    "0",
                    "false",
                    "no",
                    "off",
                }
            ),
        )

    @property
    def api_key_configured(
        self,
    ):
        return bool(
            os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def to_dict(self):
        return {
            "model": self.model,
            "enabled": self.enabled,
            "api_key_configured": (
                self.api_key_configured
            ),
        }


openai_config = (
    OpenAIConfig
    .from_environment()
      )
