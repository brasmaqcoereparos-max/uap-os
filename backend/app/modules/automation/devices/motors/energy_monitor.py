class EnergyMonitor:

    def __init__(self):

        self.voltage = 0

        self.current = 0

    def power(self):

        return self.voltage * self.current

    def set_voltage(

        self,

        voltage,

    ):

        self.voltage = voltage

    def set_current(

        self,

        current,

    ):

        self.current = current
