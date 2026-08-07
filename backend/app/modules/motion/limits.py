class AxisLimits:

    def check(

        self,

        axis,

        value,

    ):

        if axis.limit_min is not None:

            if value < axis.limit_min:

                return False

        if axis.limit_max is not None:

            if value > axis.limit_max:

                return False

        return True


axis_limits = AxisLimits()
