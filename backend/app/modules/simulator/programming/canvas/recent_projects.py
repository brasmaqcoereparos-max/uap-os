from datetime import datetime


class RecentProjects:

    def __init__(self):

        self.projects = []

        self.limit = 10

    def add(self, path):

        self.projects.insert(

            0,

            {
                "path": path,
                "date": datetime.now().isoformat(),
            },

        )

        self.projects = self.projects[: self.limit]

    def all(self):

        return self.projects


recent_projects = RecentProjects()
