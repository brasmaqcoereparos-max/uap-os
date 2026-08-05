class Rotation:

    @staticmethod
    def rotate(

        component,

        angle,

    ):

        component.rotation = (

            component.rotation + angle

        ) % 360
