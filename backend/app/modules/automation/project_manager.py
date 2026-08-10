class AutomationProjectManager:

    def __init__(self):

        self.projects = {}

    def add(
        self,
        project,
    ):

        self.projects[
            project.name
        ] = project

    def remove(
        self,
        name,
    ):

        self.projects.pop(
            name,
            None,
        )

    def get(
        self,
        name,
    ):

        return self.projects.get(
            name
        )

    def list(self):

        return list(
            self.projects.values()
        )


project_manager = AutomationProjectManager()
