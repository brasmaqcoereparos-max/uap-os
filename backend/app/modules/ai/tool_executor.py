from app.modules.ai.tool_call import (
    AIToolCall,
)
from app.modules.ai.tool_result import (
    AIToolResult,
)


class AIToolExecutor:

    def execute(
        self,
        call: AIToolCall,
    ):
        return AIToolResult(
            tool=call.tool,
            success=True,
            result={
                "status": "proposed",
                "target": call.tool,
                "arguments": dict(
                    call.arguments
                ),
            },
            metadata={
                "simulation": True,
                "direct_hardware": False,
            },
        )


ai_tool_executor = (
    AIToolExecutor()
)
