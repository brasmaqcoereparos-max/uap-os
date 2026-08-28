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
    DIGITAL = "digital"
    ANALOG = "analog"
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
            cls.DIGITAL,
            cls.ANALOG,
            cls.OTHER,
        ]

    @classmethod
    def exists(cls, sensor_type):
        return (
            str(sensor_type).strip().lower()
            in cls.all()
        )

    @classmethod
    def normalize(cls, sensor_type):
        value = str(
            sensor_type or cls.OTHER
        ).strip().lower()

        if not cls.exists(value):
            return cls.OTHER

        return value
