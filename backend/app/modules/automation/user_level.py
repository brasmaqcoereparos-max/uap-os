from enum import Enum


class UserLevel(Enum):

    BEGINNER = "beginner"

    ADVANCED = "advanced"

    TECHNICAL = "technical"


class UserLevelManager:

    def __init__(self):

        self.level = UserLevel.BEGINNER

    def set(
        self,
        level,
    ):

        self.level = level

    def get(self):

        return self.level


user_level = UserLevelManager()
