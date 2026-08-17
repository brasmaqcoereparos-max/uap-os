from app.modules.automation.robot_position import (
    RobotPosition,
)


class Localization:

    def __init__(self):

        self.position = RobotPosition()

        self.valid = False

    def update(
        self,
        x,
        y,
        angle=0,
    ):

        self.position.set(
            x,
            y,
            angle,
        )

        self.valid = True

    def invalidate(self):

        self.valid = False

    def get_position(self):

        return self.position.get()

    def is_valid(self):

        return self.valid


localization = Localization()
