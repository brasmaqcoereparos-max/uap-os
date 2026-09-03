from app.modules.ai.tool_permission import (
    AIToolPermission,
)


class AIToolPermissionRegistry:

    def __init__(self):
        self._permissions: dict[
            str,
            AIToolPermission,
        ] = {}

    def register(
        self,
        permission: AIToolPermission,
    ):
        self._permissions[
            permission.tool
        ] = permission

        return permission

    def get(
        self,
        tool: str,
    ):
        return self._permissions.get(
            tool
        )

    def remove(
        self,
        tool: str,
    ):
        return self._permissions.pop(
            tool,
            None,
        )

    def list_all(self):
        return list(
            self._permissions.values()
        )

    def clear(self):
        self._permissions.clear()


ai_tool_permission_registry = (
    AIToolPermissionRegistry()
)
