class DeviceData:

    def __init__(self):

        self.tags = {}
        self.variables = {}
        self.alarms = {}

    def set_tag(
        self,
        name,
        value,
    ):

        self.tags[name] = value

    def get_tag(
        self,
        name,
        default=None,
    ):

        return self.tags.get(
            name,
            default,
        )

    def set_variable(
        self,
        name,
        value,
    ):

        self.variables[name] = value

    def get_variable(
        self,
        name,
        default=None,
    ):

        return self.variables.get(
            name,
            default,
        )

    def add_alarm(
        self,
        alarm,
    ):

        self.alarms[alarm.name] = alarm

    def active_alarms(self):

        return [
            alarm
            for alarm in self.alarms.values()
            if alarm.active
          ]
