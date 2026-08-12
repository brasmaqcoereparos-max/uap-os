class RobotUIActions:

    JOG = "jog"
    RECORD = "record"
    EDIT = "edit"
    DELETE = "delete"
    PLAY = "play"
    PAUSE = "pause"
    STOP = "stop"
    SAVE = "save"
    HOME = "home"
    EMERGENCY_STOP = "emergency_stop"

    @classmethod
    def all(cls):

        return [
            cls.JOG,
            cls.RECORD,
            cls.EDIT,
            cls.DELETE,
            cls.PLAY,
            cls.PAUSE,
            cls.STOP,
            cls.SAVE,
            cls.HOME,
            cls.EMERGENCY_STOP,
        ]
