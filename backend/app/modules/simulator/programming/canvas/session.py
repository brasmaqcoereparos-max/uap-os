from datetime import datetime


class Session:

    def __init__(self):

        self.started = datetime.now()

        self.project = None

        self.modified = False

    def open_project(self, name):

        self.project = name

        self.modified = False

    def mark_modified(self):

        self.modified = True

    def save(self):

        self.modified = False

    def to_dict(self):

        return {
            "started": self.started.isoformat(),
            "project": self.project,
            "modified": self.modified,
        }


session = Session()
