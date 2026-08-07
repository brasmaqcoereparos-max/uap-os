from enum import Enum


class InterpolationMode(Enum):

    NONE = "none"

    JOINT = "joint"

    LINEAR = "linear"

    CIRCULAR = "circular"

    SPLINE = "spline"

    BEZIER = "bezier"


class MotionInterpolation:

    def __init__(self):

        self.mode = InterpolationMode.JOINT

    def set_mode(

        self,

        mode,

    ):

        self.mode = mode

    def get_mode(self):

        return self.mode


motion_interpolation = MotionInterpolation()
