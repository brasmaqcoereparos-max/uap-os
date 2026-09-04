from typing import Any

from app.modules.ai.safety_finding import (
    AISafetyFinding,
)
from app.modules.ai.safety_level import (
    AISafetyLevel,
)
from app.modules.ai.safety_policy import (
    ai_safety_policy,
)
from app.modules.ai.safety_result import (
    AISafetyResult,
)


class AIProposalValidator:

    def validate(
        self,
        data: dict[
            str,
            Any,
        ],
    ):
        result = AISafetyResult(
            level=AISafetyLevel.SAFE
        )

        self._inspect(
            value=data,
            path="root",
            result=result,
        )

        return result

    def _inspect(
        self,
        value: Any,
        path: str,
        result: AISafetyResult,
    ):
        if isinstance(
            value,
            dict,
        ):
            for key, item in (
                value.items()
            ):
                key_text = str(
                    key
                ).lower()

                item_path = (
                    f"{path}.{key}"
                )

                if (
                    key_text
                    in ai_safety_policy
                    .blocked_targets
                ):
                    result.add_finding(
                        AISafetyFinding(
                            code=(
                                "direct_hardware"
                            ),
                            message=(
                                "Direct hardware "
                                "access is blocked."
                            ),
                            level="blocked",
                            path=item_path,
                        )
                    )

                if (
                    key_text
                    in ai_safety_policy
                    .review_targets
                ):
                    result.add_finding(
                        AISafetyFinding(
                            code=(
                                "review_target"
                            ),
                            message=(
                                "This target "
                                "requires review."
                            ),
                            level="warning",
                            path=item_path,
                        )
                    )

                self._inspect(
                    item,
                    item_path,
                    result,
                )

        elif isinstance(
            value,
            list,
        ):
            for index, item in (
                enumerate(value)
            ):
                self._inspect(
                    item,
                    f"{path}[{index}]",
                    result,
                )

        elif isinstance(
            value,
            str,
        ):
            lowered = (
                value.lower()
            )

            for keyword in (
                ai_safety_policy
                .destructive_keywords
            ):
                if keyword in lowered:
                    result.add_finding(
                        AISafetyFinding(
                            code=(
                                "destructive_action"
                            ),
                            message=(
                                "Potentially "
                                "destructive action."
                            ),
                            level="warning",
                            path=path,
                        )
                    )


ai_proposal_validator = (
    AIProposalValidator()
                  )
