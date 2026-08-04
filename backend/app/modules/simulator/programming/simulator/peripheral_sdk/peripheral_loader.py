class PeripheralLoader:

    loaded = False

    @classmethod
    def load(cls):

        if cls.loaded:

            return

        cls.loaded = True
