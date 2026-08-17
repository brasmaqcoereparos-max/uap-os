class CleaningActuatorTypes:

    BRUSH = "brush"

    VACUUM = "vacuum"

    WATER_PUMP = "water_pump"

    DETERGENT_PUMP = "detergent_pump"

    AIR_PUMP = "air_pump"

    DRYER = "dryer"

    SPRAYER = "sprayer"

    WHEEL = "wheel"

    @classmethod
    def all(cls):

        return [
            cls.BRUSH,
            cls.VACUUM,
            cls.WATER_PUMP,
            cls.DETERGENT_PUMP,
            cls.AIR_PUMP,
            cls.DRYER,
            cls.SPRAYER,
            cls.WHEEL,
        ]
