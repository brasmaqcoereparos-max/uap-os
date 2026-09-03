from app.modules.ai.tool_call import (
    AIToolCall,
)
from app.modules.ai.tool_permission_registry import (
    ai_tool_permission_registry,
)
from app.modules.ai.tool_registry import (
    ai_tool_registry,
)


class AIToolValidator:

    def validate(
        self,
        call: AIToolCall,
    ):
        errors = []

        tool = ai_tool_registry.get(
            call.tool
        )

        if not tool:
            errors.append(
                "AI tool not found"
            )

            return {
                "valid": False,
                "errors": errors,
                "requires_review": True,
            }

        if not tool.enabled:
            errors.append(
                "AI tool is disabled"
            )

        permission = (
            ai_tool_permission_registry
            .get(call.tool)
        )

        if not permission:
            errors.append(
                "AI tool permission "
                "not found"
            )

            return {
                "valid": False,
                "errors": errors,
                "requires_review": True,
            }

        if not permission.allows(
            call.source
        ):
            errors.append(
                "AI tool source "
                "is not allowed"
            )

        requires_review = (
            tool.requires_review
            or permission.requires_review
        )

        return {
            "valid": not errors,
            "errors": errors,
            "requires_review": (
                requires_review
            ),
        }


ai_tool_validator = (
    AIToolValidator()
        )
