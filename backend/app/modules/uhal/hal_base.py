class UHALBase:

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def digital_write(self, pin, value):
        pass

    def digital_read(self, pin):
        return 0

    def analog_read(self, pin):
        return 0

    def analog_write(self, pin, value):
        pass

    def pwm_write(self, pin, duty):
        pass

    def pwm_frequency(self, pin, frequency):
        pass
