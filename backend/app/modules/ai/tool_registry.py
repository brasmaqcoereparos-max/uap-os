from app.modules.ai.tool_definition import (
    AIToolDefinition,
)


class AIToolRegistry:

    def __init__(self):
        self._tools: dict[
            str,
            AIToolDefinition,
        ] = {}

    def register(
        self,
        tool: AIToolDefinition,
    ):
        self._tools[
            tool.name
        ] = tool

        return tool

    def get(
        self,
        name: str,
    ):
        return self._tools.get(
            name
        )

    def remove(
        self,
        name: str,
    ):
        return self._tools.pop(
            name,
            None,
        )

    def list_all(self):
        return list(
            self._tools.values()
        )

    def enabled(self):
        return [
            tool
            for tool
            in self._tools.values()
            if tool.enabled
        ]

    def clear(self):
        self._tools.clear()


ai_tool_registry = (
    AIToolRegistry()
)
