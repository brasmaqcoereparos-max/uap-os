class RobotUIPanel:

    def __init__(self):

        self.sections = [
            "robot_status",
            "axis_control",
            "joystick",
            "pose_list",
            "program_control",
            "safety",
        ]

    def get_sections(self):

        return list(self.sections)

    def has_section(self, name):

        return name in self.sections


robot_ui_panel = RobotUIPanel()
