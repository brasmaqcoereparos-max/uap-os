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
    QR_CODE = "qr_code"
    BARCODE = "barcode"
    TEXT = "text"
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
            cls.QR_CODE,
            cls.BARCODE,
            cls.TEXT,
            cls.UNKNOWN,
        ]

    @classmethod
    def exists(cls, vision_type):
        return (
            str(
                vision_type
            ).strip().lower()
            in cls.all()
        )

    @classmethod
    def normalize(cls, vision_type):
        value = str(
            vision_type
            or cls.UNKNOWN
        ).strip().lower()

        if not cls.exists(value):
            return cls.UNKNOWN

        return value
