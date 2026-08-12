from app.modules.automation.robot_ui_model import (
    RobotUIModel,
)


class RobotUIController:

    def __init__(self):

        self.model = RobotUIModel()

    def update_axes(self, axes):

        self.model.set_axes(axes)

    def select_pose(self, index):

        self.model.select_pose(index)

    def set_mode(self, mode):

        self.model.set_mode(mode)

    def get_state(self):

        return self.model.get_state()


robot_ui_controller = RobotUIController()
