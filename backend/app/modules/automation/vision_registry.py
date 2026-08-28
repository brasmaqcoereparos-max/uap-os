class VisionRegistry:
    def __init__(self):
        self.detectors = {}

    def register(
        self,
        name,
        detector,
        replace=True,
    ):
        name = str(name)

        if (
            name in self.detectors
            and not replace
        ):
            raise ValueError(
                "Detector já registrado: "
                f"{name}"
            )

        self.detectors[
            name
        ] = detector

        return detector

    def unregister(self, name):
        return self.detectors.pop(
            str(name),
            None,
        )

    def get(self, name):
        return self.detectors.get(
            str(name)
        )

    def exists(self, name):
        return (
            str(name)
            in self.detectors
        )

    def get_all(self):
        return dict(
            self.detectors
        )

    def all(self):
        return list(
            self.detectors.values()
        )

    def names(self):
        return list(
            self.detectors.keys()
        )

    def clear(self):
        count = len(
            self.detectors
        )

        self.detectors.clear()

        return count

    def count(self):
        return len(
            self.detectors
        )


vision_registry = VisionRegistry()
