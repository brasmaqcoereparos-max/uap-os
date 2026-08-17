class CleaningTypes:

    VACUUM = "vacuum"

    SWEEP = "sweep"

    MOP = "mop"

    WASH = "wash"

    SCRUB = "scrub"

    DRY = "dry"

    GENERAL = "general"

    @classmethod
    def all(cls):

        return [
            cls.VACUUM,
            cls.SWEEP,
            cls.MOP,
            cls.WASH,
            cls.SCRUB,
            cls.DRY,
            cls.GENERAL,
        ]
