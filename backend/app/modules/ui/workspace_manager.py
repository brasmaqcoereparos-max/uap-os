from __future__ import annotations

from app.modules.ui.workspace import (
    UIWorkspace,
)


class UIWorkspaceManager:

    def __init__(self):
        self._workspaces: dict[
            str,
            UIWorkspace,
        ] = {}

        self._active_id: (
            str | None
        ) = None

    @property
    def active_id(self):
        return self._active_id

    def register(
        self,
        workspace: UIWorkspace,
    ):
        self._workspaces[
            workspace.id
        ] = workspace

        if self._active_id is None:
            self._active_id = (
                workspace.id
            )

        return workspace

    def create(
        self,
        workspace_id: str,
        name: str,
        user_level: str = "beginner",
        readonly: bool = False,
    ) -> UIWorkspace:
        if workspace_id in self._workspaces:
            raise ValueError(
                "Workspace already exists: "
                f"{workspace_id}"
            )

        workspace = UIWorkspace(
            id=workspace_id,
            name=name,
            user_level=user_level,
            readonly=readonly,
        )

        return self.register(
            workspace
        )

    def get(
        self,
        workspace_id: str,
    ):
        return self._workspaces.get(
            workspace_id
        )

    def active(self):
        if self._active_id is None:
            return None

        return self.get(
            self._active_id
        )

    def activate(
        self,
        workspace_id: str,
    ):
        if (
            workspace_id
            not in self._workspaces
        ):
            return False

        self._active_id = (
            workspace_id
        )

        return True

    def set_active_level(
        self,
        level: str,
    ) -> str:
        workspace = self.active()

        if workspace is None:
            raise RuntimeError(
                "No active workspace"
            )

        return workspace.set_user_level(
            level
        )

    def remove(
        self,
        workspace_id: str,
    ):
        workspace = (
            self._workspaces.pop(
                workspace_id,
                None,
            )
        )

        if (
            workspace
            and self._active_id
            == workspace_id
        ):
            self._active_id = (
                next(
                    iter(
                        self._workspaces
                    ),
                    None,
                )
            )

        return workspace

    def list_all(self):
        return list(
            self._workspaces.values()
        )

    def clear(self) -> None:
        self._workspaces.clear()
        self._active_id = None

    def snapshot(self) -> dict:
        return {
            "active_id": self._active_id,
            "workspaces": [
                workspace.to_dict()
                for workspace
                in self.list_all()
            ],
        }


ui_workspace_manager = (
    UIWorkspaceManager()
            )
