class AutomationProjectManager:
    def __init__(self):
        self.projects = {}

    @staticmethod
    def _key(project):
        project_id = getattr(
            project,
            "project_id",
            None,
        )

        if project_id:
            return str(project_id)

        name = getattr(
            project,
            "name",
            None,
        )

        if not name:
            raise ValueError(
                "Projeto sem ID ou nome."
            )

        return str(name)

    def add(
        self,
        project,
        replace=True,
    ):
        key = self._key(project)

        if (
            key in self.projects
            and not replace
        ):
            raise ValueError(
                f"Projeto já existe: {key}"
            )

        self.projects[key] = project

        return project

    def remove(self, identifier):
        identifier = str(identifier)

        if identifier in self.projects:
            return self.projects.pop(
                identifier
            )

        for key, project in list(
            self.projects.items()
        ):
            if str(
                getattr(
                    project,
                    "name",
                    "",
                )
            ) == identifier:
                return self.projects.pop(
                    key
                )

        return None

    def get(self, identifier):
        identifier = str(identifier)

        project = self.projects.get(
            identifier
        )

        if project is not None:
            return project

        for item in self.projects.values():
            if str(
                getattr(
                    item,
                    "name",
                    "",
                )
            ) == identifier:
                return item

        return None

    def exists(self, identifier):
        return (
            self.get(identifier)
            is not None
        )

    def list(self):
        return list(
            self.projects.values()
        )

    def clear(self):
        count = len(self.projects)
        self.projects.clear()
        return count

    def count(self):
        return len(self.projects)


project_manager = (
    AutomationProjectManager()
            )
