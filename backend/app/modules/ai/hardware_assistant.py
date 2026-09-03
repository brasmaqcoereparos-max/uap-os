from app.modules.ai.hardware_matcher import (
    ai_hardware_matcher,
)
from app.modules.ai.hardware_requirement import (
    AIHardwareRequirement,
)


class AIHardwareAssistant:

    def recommend(
        self,
        requirement: (
            AIHardwareRequirement
        ),
        boards: list[dict],
    ):
        candidates = []

        for board in boards:
            candidate = (
                ai_hardware_matcher
                .evaluate(
                    board_id=str(
                        board.get(
                            "id",
                            "",
                        )
                    ),
                    board_name=str(
                        board.get(
                            "name",
                            "Unknown Board",
                        )
                    ),
                    capabilities=dict(
                        board.get(
                            "capabilities",
                            {},
                        )
                    ),
                    requirement=(
                        requirement
                    ),
                )
            )

            candidates.append(
                candidate
            )

        candidates.sort(
            key=lambda item: (
                item.compatible,
                item.score,
            ),
            reverse=True,
        )

        return candidates


ai_hardware_assistant = (
    AIHardwareAssistant()
)
