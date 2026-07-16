from datetime import datetime


class AutoSave:

    def __init__(self):

        self.enabled = True

        self.interval = 300

        self.last_save = None

    def save(self):

        self.last_save = datetime.now()

    def set_interval(self, seconds):

        if seconds < 30:
            seconds = 30

        self.interval = seconds

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def to_dict(self):

        return {
            "enabled": self.enabled,
            "interval": self.interval,
            "last_save": (
                self.last_save.isoformat()
                if self.last_save
                else None
            ),
        }


autosave = AutoSave()
