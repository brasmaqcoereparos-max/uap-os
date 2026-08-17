class CleaningTask:

    def __init__(
        self,
        task_id,
        name,
        cleaning_type="general",
    ):

        self.task_id = task_id
        self.name = name
        self.cleaning_type = cleaning_type

        self.area = None
        self.priority = 0
        self.completed = False
        self.enabled = True

    def set_area(self, area):

        self.area = area

    def set_priority(self, priority):

        self.priority = priority

    def complete(self):

        self.completed = True

    def reset(self):

        self.completed = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def to_dict(self):

        return {
            "id": self.task_id,
            "name": self.name,
            "cleaning_type": self.cleaning_type,
            "area": self.area,
            "priority": self.priority,
            "completed": self.completed,
            "enabled": self.enabled,
        }
