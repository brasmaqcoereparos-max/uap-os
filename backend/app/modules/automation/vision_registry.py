class VisionRegistry:

    def __init__(self):

        self.detectors = {}

    def register(
        self,
        name,
        detector,
    ):

        self.detectors[name] = detector

    def unregister(self, name):

        self.detectors.pop(
            name,
            None,
        )

    def get(self, name):

        return self.detectors.get(name)

    def exists(self, name):

        return name in self.detectors

    def get_all(self):

        return dict(self.detectors)


vision_registry = VisionRegistry()
