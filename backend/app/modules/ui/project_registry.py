from app.modules.ui.project_state import (
    UIProjectState,
)


class UIProjectRegistry:

    def __init__(self):
        self._projects: dict[
            str,
            UIProjectState,
        ] = {}

    def register(
        self,
        project: UIProjectState,
    ):
        self._projects[
            project.project_id
        ] = project

        return project

    def get(
        self,
        project_id: str,
    ):
        return self._projects.get(
            project_id
        )

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

    def remove(
        self,
        project_id: str,
    ):
        return self._projects.pop(
            project_id,
            None,
        )

    def list_all(self):
        return list(
            self._projects.values()
        )

    def clear(self):
        self._projects.clear()


ui_project_registry = (
    UIProjectRegistry()
    )
