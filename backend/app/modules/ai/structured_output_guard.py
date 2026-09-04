from typing import Any

from app.modules.ai.proposal_validator import (
    ai_proposal_validator,
)
from app.modules.ai.schema_guard import (
    ai_schema_guard,
)


class AIStructuredOutputGuard:

    def validate(
        self,
        data: dict[
            str,
            Any,
        ],
        required_keys: (
            list[str] | None
        ) = None,
    ):
        schema = {
            "valid": True,
            "missing": [],
        }

        if required_keys:
            schema = (
                ai_schema_guard
                .require_keys(
                    data,
                    required_keys,
                )
            )

        safety = (
            ai_proposal_validator
            .validate(data)
        )

        valid = (
            schema["valid"]
            and safety.level.value
            != "blocked"
        )

        return {
            "valid": valid,
            "schema": schema,
            "safety": (
                safety.to_dict()
            ),
        }


ai_structured_output_guard = (
    AIStructuredOutputGuard()
)
