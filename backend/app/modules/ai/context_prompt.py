class AIContextPrompt:

    @staticmethod
    def build(
        context,
    ):
        if context is None:
            return ""

        parts = []

        user_level = getattr(
            context,
            "user_level",
            None,
        )

        if user_level:
            value = (
                user_level.value
                if hasattr(
                    user_level,
                    "value",
                )
                else str(
                    user_level
                )
            )

            parts.append(
                "User level: "
                f"{value}"
            )

        project_id = getattr(
            context,
            "project_id",
            None,
        )

        if project_id:
            parts.append(
                "Project ID: "
                f"{project_id}"
            )

        data = getattr(
            context,
            "data",
            None,
        )

        if isinstance(
            data,
            dict,
        ):
            for key, value in (
                data.items()
            ):
                parts.append(
                    f"{key}: {value}"
                )

        return "\n".join(parts)


ai_context_prompt = (
    AIContextPrompt()
)
