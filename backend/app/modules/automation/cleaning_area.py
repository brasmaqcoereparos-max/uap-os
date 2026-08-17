class CleaningArea:

    def __init__(
        self,
        area_id,
        name,
    ):

        self.area_id = area_id
        self.name = name

        self.enabled = True
        self.priority = 0

        self.cleaning_type = "general"

    def set_priority(self, priority):

        self.priority = priority

    def set_cleaning_type(
        self,
        cleaning_type,
    ):

        self.cleaning_type = cleaning_type

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def to_dict(self):

        return {
            "id": self.area_id,
            "name": self.name,
            "enabled": self.enabled,
            "priority": self.priority,
            "cleaning_type":
                self.cleaning_type,
        }
