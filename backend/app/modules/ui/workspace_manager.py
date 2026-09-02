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


ui_workspace_manager = (
    UIWorkspaceManager()
  )
