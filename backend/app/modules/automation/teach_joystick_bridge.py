class TeachJoystickBridge:

    def __init__(
        self,
        joystick,
        robot,
    ):

        self.joystick = joystick
        self.robot = robot

    def get_commands(self):

        return self.joystick.get_axes()

    def apply_positions(
        self,
        positions,
    ):

        for axis_id, position in positions.items():

            self.robot.set_position(
                axis_id,
                position,
            )
