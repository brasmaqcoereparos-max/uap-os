from datetime import datetime


class ProjectInfo:

    def __init__(self):

        self.name = "Novo Projeto"

        self.author = ""

        self.version = "1.0.0"

        self.created = datetime.now()

        self.modified = datetime.now()

    def touch(self):

        self.modified = datetime.now()

    def to_dict(self):

        return {
            "name": self.name,
            "author": self.author,
            "version": self.version,
            "created": self.created.isoformat(),
            "modified": self.modified.isoformat(),
        }


project_info = ProjectInfo()
