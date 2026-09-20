from __future__ import annotations

from typing import Any


class AIContextPrompt:

    LEVEL_INSTRUCTIONS = {
        "beginner": (
            "Use simple language, visual "
            "concepts and guided steps. "
            "Do not require textual "
            "programming knowledge."
        ),
        "intermediate": (
            "Explain blocks, conditions, "
            "events, sensors, actuators, "
            "parameters and flows."
        ),
        "professional": (
            "Allow advanced technical "
            "details including graphs, "
            "functions, protocols, targets "
            "and hardware configuration."
        ),
    }

    @staticmethod
    def _value(
        value: Any,
    ) -> Any:
        if hasattr(
            value,
            "value",
        ):
            return value.value

        return value

    def user_level(
        self,
        context,
    ) -> str:
        if context is None:
            return "beginner"

        direct = getattr(
            context,
            "user_level",
            None,
        )

        if direct:
            return str(
                self._value(
                    direct
                )
            ).lower()

        user_context = getattr(
            context,
            "user_context",
            {},
        )

        if isinstance(
            user_context,
            dict,
        ):
            level = (
                user_context.get(
                    "level"
                )
            )

            if level:
                return str(
                    self._value(
                        level
                    )
                ).lower()

        return "beginner"

    def build(
        self,
        context,
    ) -> str:
        if context is None:
            return ""

        parts: list[str] = []

        level = self.user_level(
            context
        )

        parts.append(
            "User level: "
            f"{level}"
        )

        instruction = (
            self.LEVEL_INSTRUCTIONS
            .get(
                level
            )
        )

        if instruction:
            parts.append(
                "Interaction mode: "
                f"{instruction}"
            )

        project_id = getattr(
            context,
            "project_id",
            None,
        )

        project_context = getattr(
            context,
            "project_context",
            {},
        )

        if (
            not project_id
            and isinstance(
                project_context,
                dict,
            )
        ):
            project_id = (
                project_context.get(
                    "project_id"
                )
            )

        if project_id:
            parts.append(
                "Project ID: "
                f"{project_id}"
            )

        if isinstance(
            project_context,
            dict,
        ):
            project_data = (
                project_context.get(
                    "data",
                    {},
                )
            )

            if isinstance(
                project_data,
                dict,
            ):
                for (
                    key,
                    value,
                ) in (
                    project_data.items()
                ):
                    parts.append(
                        "Project "
                        f"{key}: {value}"
                    )

        intent_context = getattr(
            context,
            "intent_context",
            {},
        )

        if isinstance(
            intent_context,
            dict,
        ):
            intent = (
                intent_context.get(
                    "intent"
                )
            )

            confidence = (
                intent_context.get(
                    "confidence"
                )
            )

            if intent:
                parts.append(
                    "Current intent: "
                    f"{intent}"
                )

            if confidence is not None:
                parts.append(
                    "Intent confidence: "
                    f"{confidence}"
                )

        short_term = getattr(
            context,
            "short_term",
            {},
        )

        if isinstance(
            short_term,
            dict,
        ):
            for (
                key,
                value,
            ) in short_term.items():
                parts.append(
                    "Context "
                    f"{key}: {value}"
                )

        legacy_data = getattr(
            context,
            "data",
            None,
        )

        if isinstance(
            legacy_data,
            dict,
        ):
            for (
                key,
                value,
            ) in legacy_data.items():
                parts.append(
                    f"{key}: {value}"
                )

        parts.extend(
            [
                (
                    "AI proposals must be "
                    "reviewable before execution."
                ),
                (
                    "Do not bypass Runtime, "
                    "Safety or UHAL to control "
                    "physical hardware."
                ),
                (
                    "Prefer simulation and "
                    "validation before deployment."
                ),
            ]
        )

        return "\n".join(
            parts
        )


ai_context_prompt = (
    AIContextPrompt()
        )
