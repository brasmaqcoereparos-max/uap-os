from app.modules.automation.joystick_controller import (
    JoystickController,
)

from app.modules.automation.teach_mode import (
    teach_mode,
)


class JoystickTeach:

    def __init__(self):

        self.joystick = JoystickController()

    def enable(self):

        teach_mode.enable()

    def disable(self):

        teach_mode.disable()

    def update(
        self,
        axis,
        value,
    ):

        if not teach_mode.is_enabled():
            return False

        self.joystick.set_axis(
            axis,
            value,
        )

        return True

    def get_axes(self):

        return self.joystick.get_axes()


joystick_teach = JoystickTeach()
