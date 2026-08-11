class MotionInterpolation:

    def calculate(
        self,
        start,
        end,
        steps,
    ):

        if steps <= 0:
            return []

        result = []

        for index in range(1, steps + 1):

            ratio = index / steps

            position = {}

            for axis in start:

                start_value = start[axis]
                end_value = end.get(
                    axis,
                    start_value,
                )

                position[axis] = (
                    start_value
                    + (
                        end_value
                        - start_value
                    )
                    * ratio
                )

            result.append(position)

        return result
