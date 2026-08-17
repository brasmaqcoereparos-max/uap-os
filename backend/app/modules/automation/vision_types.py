class VisionTypes:

    CAMERA = "camera"

    OBJECT = "object"

    PERSON = "person"

    OBSTACLE = "obstacle"

    WALL = "wall"

    FLOOR = "floor"

    MARKER = "marker"

    DIRT = "dirt"

    AREA = "area"

    UNKNOWN = "unknown"

    @classmethod
    def all(cls):

        return [
            cls.CAMERA,
            cls.OBJECT,
            cls.PERSON,
            cls.OBSTACLE,
            cls.WALL,
            cls.FLOOR,
            cls.MARKER,
            cls.DIRT,
            cls.AREA,
            cls.UNKNOWN,
        ]
