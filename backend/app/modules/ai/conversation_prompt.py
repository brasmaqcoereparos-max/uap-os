from app.modules.ai.schemas import (
    MessageRole,
)


class AIConversationPrompt:

    @staticmethod
    def messages(
        conversation,
        limit: int = 12,
    ):
        if conversation is None:
            return []

        source = list(
            getattr(
                conversation,
                "messages",
                [],
            )
        )

        if limit > 0:
            source = source[
                -limit:
            ]

        result = []

        for message in source:
            role = getattr(
                message,
                "role",
                MessageRole.USER,
            )

            content = getattr(
                message,
                "content",
                "",
            )

            result.append(
                {
                    "role": role,
                    "content": content,
                }
            )

        return result


ai_conversation_prompt = (
    AIConversationPrompt()
          )
