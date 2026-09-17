from __future__ import annotations

from app.modules.ui.project_state import (
    UIProjectState,
)


class UIProjectRegistry:

    def __init__(self):
        self._projects: dict[
            str,
            UIProjectState,
        ] = {}

        self._active_project_id: (
            str | None
        ) = None

    def register(
        self,
        project: UIProjectState,
    ):
        self._projects[
            project.project_id
        ] = project

        if (
            self._active_project_id
            is None
        ):
            self._active_project_id = (
                project.project_id
            )

        return project

    def get(
        self,
        project_id: str,
    ):
        return self._projects.get(
            project_id
        )

    def require(
        self,
        project_id: str,
    ) -> UIProjectState:
        project = self.get(
            project_id
        )

        if project is None:
            raise KeyError(
                "UI project not found: "
                f"{project_id}"
            )

        return project

    def get_or_create(
        self,
        project_id: str,
    ):
        project = self.get(
            project_id
        )

        if project:
            return project

        project = UIProjectState(
            project_id=project_id
        )

        return self.register(
            project
        )

    def activate(
        self,
        project_id: str,
    ) -> UIProjectState:
        project = self.require(
            project_id
        )

        self._active_project_id = (
            project_id
        )

        return project

    def active(
        self,
    ) -> UIProjectState | None:
        if (
            self._active_project_id
            is None
        ):
            return None

        return self.get(
            self._active_project_id
        )

    def remove(
        self,
        project_id: str,
    ):
        project = self._projects.pop(
            project_id,
            None,
        )

        if (
            project is not None
            and self._active_project_id
            == project_id
        ):
            self._active_project_id = (
                next(
                    iter(
                        self._projects
                    ),
                    None,
                )
            )

        return project

    def list_all(self):
        return list(
            self._projects.values()
        )

    def snapshot(self):
        return {
            "active_project_id": (
                self._active_project_id
            ),
            "projects": [
                project.to_dict()
                for project
                in self.list_all()
            ],
        }

    def clear(self):
        self._projects.clear()
        self._active_project_id = None


ui_project_registry = (
    UIProjectRegistry()
            )
