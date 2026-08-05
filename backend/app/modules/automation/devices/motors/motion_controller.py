from app.modules.automation.devices.motors.multi_axis_controller import (
    multi_axis_controller,
)


class MotionController:

    def home_all(self):

        for axis in multi_axis_controller.all_axes():

            axis.move_to(0)

    def move_all(

        self,

        positions,

    ):

        for name, position in positions.items():

            axis = multi_axis_controller.get_axis(name)

            if axis:

                axis.move_to(position)


motion_controller = MotionController()
