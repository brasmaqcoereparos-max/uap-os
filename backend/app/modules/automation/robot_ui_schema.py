class RobotUISchema:

    def build(self, state):

        return {
            "title": state["name"],
            "mode": state["mode"],
            "axes": state["axes"],
            "selected_pose": state[
                "selected_pose"
            ],
            "sections": [
                "status",
                "axes",
                "joystick",
                "positions",
                "program",
                "safety",
            ],
        }


robot_ui_schema = RobotUISchema()
