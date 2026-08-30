"""
Utilitários de rotação para componentes visuais.
"""


class Rotation:

    VALID_ANGLES = {
        0,
        90,
        180,
        270,
    }

    @staticmethod
    def normalize(
        angle,
    ):
        return float(
            angle
        ) % 360

    @classmethod
    def rotate(
        cls,
        component,
        angle,
    ):
        if component is None:
            return None

        current = float(
            getattr(
                component,
                "rotation",
                0,
            )
        )

        new_angle = (
            current
            + float(angle)
        ) % 360

        setter = getattr(
            component,
            "set_rotation",
            None,
        )

        if callable(setter):
            setter(new_angle)

        else:
            component.rotation = (
                new_angle
            )

        return new_angle

    @classmethod
    def set(
        cls,
        component,
        angle,
    ):
        if component is None:
            return None

        angle = cls.normalize(
            angle
        )

        setter = getattr(
            component,
            "set_rotation",
            None,
        )

        if callable(setter):
            setter(angle)

        else:
            component.rotation = angle

        return angle

    @classmethod
    def rotate_clockwise(
        cls,
        component,
        step=90,
    ):
        return cls.rotate(
            component,
            abs(float(step)),
        )

    @classmethod
    def rotate_counterclockwise(
        cls,
        component,
        step=90,
    ):
        return cls.rotate(
            component,
            -abs(float(step)),
        )

    @staticmethod
    def is_cardinal(
        angle,
    ):
        angle = (
            float(angle)
            % 360
        )

        return angle in (
            Rotation.VALID_ANGLES
        )
