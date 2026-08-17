class CleaningAction:

    MOVE = "move"
    BRUSH = "brush"
    VACUUM = "vacuum"
    WATER = "water"
    DETERGENT = "detergent"
    DRY = "dry"
    STOP = "stop"
    RETURN_BASE = "return_base"

    def __init__(
        self,
        action,
        value=None,
    ):

        self.action = action
        self.value = value

    def to_dict(self):

        return {
            "action": self.action,
            "value": self.value,
        }
