class SensorTypes:

    DISTANCE = "distance"

    OBSTACLE = "obstacle"

    INFRARED = "infrared"

    ULTRASONIC = "ultrasonic"

    LIMIT = "limit"

    PROXIMITY = "proximity"

    TEMPERATURE = "temperature"

    HUMIDITY = "humidity"

    LIGHT = "light"

    PRESSURE = "pressure"

    ENCODER = "encoder"

    IMU = "imu"

    CAMERA = "camera"

    OTHER = "other"

    @classmethod
    def all(cls):

        return [
            cls.DISTANCE,
            cls.OBSTACLE,
            cls.INFRARED,
            cls.ULTRASONIC,
            cls.LIMIT,
            cls.PROXIMITY,
            cls.TEMPERATURE,
            cls.HUMIDITY,
            cls.LIGHT,
            cls.PRESSURE,
            cls.ENCODER,
            cls.IMU,
            cls.CAMERA,
            cls.OTHER,
        ]
