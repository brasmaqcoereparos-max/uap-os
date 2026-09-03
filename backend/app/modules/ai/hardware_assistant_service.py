from app.modules.ai.hardware_assistant import (
    ai_hardware_assistant,
)
from app.modules.ai.hardware_requirement import (
    AIHardwareRequirement,
)


class AIHardwareAssistantService:

    def recommend(
        self,
        requirements: dict,
        boards: list[dict],
    ):
        requirement = (
            AIHardwareRequirement(
                gpio=int(
                    requirements.get(
                        "gpio",
                        0,
                    )
                ),
                pwm=int(
                    requirements.get(
                        "pwm",
                        0,
                    )
                ),
                adc=int(
                    requirements.get(
                        "adc",
                        0,
                    )
                ),
                i2c=int(
                    requirements.get(
                        "i2c",
                        0,
                    )
                ),
                spi=int(
                    requirements.get(
                        "spi",
                        0,
                    )
                ),
                uart=int(
                    requirements.get(
                        "uart",
                        0,
                    )
                ),
                wifi=bool(
                    requirements.get(
                        "wifi",
                        False,
                    )
                ),
                bluetooth=bool(
                    requirements.get(
                        "bluetooth",
                        False,
                    )
                ),
                minimum_memory_mb=int(
                    requirements.get(
                        "minimum_memory_mb",
                        0,
                    )
                ),
            )
        )

        candidates = (
            ai_hardware_assistant
            .recommend(
                requirement=(
                    requirement
                ),
                boards=boards,
            )
        )

        return {
            "requirements": (
                requirement.to_dict()
            ),
            "candidates": [
                candidate.to_dict()
                for candidate
                in candidates
            ],
            "recommended": (
                candidates[0].to_dict()
                if candidates
                else None
            ),
        }


ai_hardware_assistant_service = (
    AIHardwareAssistantService()
                )
