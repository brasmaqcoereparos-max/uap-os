class DeviceSimulator:

    def __init__(self):

        self.running = False

    def start(self):

        self.running = True

    def stop(self):

        self.running = False

    def reset(self):

        self.running = False

    def status(self):

        return {

            "running": self.running,

        }


device_simulator = DeviceSimulator()
