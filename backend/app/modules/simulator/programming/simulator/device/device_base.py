"""
Classe base para dispositivos do simulador UAP.
"""


class DeviceBase:

    def __init__(
        self,
        name,
    ):

        self.name = name
        self.enabled = True

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def is_enabled(self):

        return self.enabled

    def update(self):
        pass

    def reset(self):
        pass
