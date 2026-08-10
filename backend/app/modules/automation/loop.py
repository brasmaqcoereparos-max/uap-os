class AutomationLoop:

    def __init__(self):

        self.enabled = False

    def start(self):

        self.enabled = True

    def stop(self):

        self.enabled = False

    def is_running(self):

        return self.enabled
