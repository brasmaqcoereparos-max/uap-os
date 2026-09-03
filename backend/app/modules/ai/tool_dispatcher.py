from app.modules.ai.tool_call import (
    AIToolCall,
)
from app.modules.ai.tool_defaults import (
    install_default_ai_tools,
)
from app.modules.ai.tool_executor import (
    ai_tool_executor,
)
from app.modules.ai.tool_validator import (
    ai_tool_validator,
)


class AIToolDispatcher:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            install_default_ai_tools()

            self._initialized = True

        return self

    def dispatch(
        self,
        call: AIToolCall,
    ):
        self.initialize()

        validation = (
            ai_tool_validator
            .validate(call)
        )

        if not validation[
            "valid"
        ]:
            return {
                "accepted": False,
                "status": "rejected",
                "validation": validation,
                "result": None,
            }

        if (
            validation[
                "requires_review"
            ]
            and not call.approved
        ):
            return {
                "accepted": True,
                "status": (
                    "review_required"
                ),
                "validation": validation,
                "result": None,
            }

        result = (
            ai_tool_executor.execute(
                call
            )
        )

        return {
            "accepted": True,
            "status": "executed",
            "validation": validation,
            "result": (
                result.to_dict()
            ),
        }


ai_tool_dispatcher = (
    AIToolDispatcher()
)
