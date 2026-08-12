class JoystickMapping:

    def __init__(self):

        self.mapping = {}

    def map_axis(
        self,
        joystick_axis,
        robot_axis,
    ):

        self.mapping[
            joystick_axis
        ] = robot_axis

    def unmap(
        self,
        joystick_axis,
    ):

        self.mapping.pop(
            joystick_axis,
            None,
        )

    def get_robot_axis(
        self,
        joystick_axis,
    ):

        return self.mapping.get(
            joystick_axis
        )

    def get_mapping(self):

        return dict(
            self.mapping
        )


joystick_mapping = JoystickMapping()
