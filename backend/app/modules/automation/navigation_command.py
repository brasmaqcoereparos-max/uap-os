class NavigationCommand:

    def __init__(
        self,
        action,
        value=0,
    ):

        self.action = action
        self.value = value

    def to_dict(self):

        return {
            "action": self.action,
            "value": self.value,
        }
