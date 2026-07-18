class CompilerPlatform:

    def __init__(self):

        self.platform = "arduino"

    def set(self, platform):

        self.platform = platform

    def get(self):

        return self.platform

    def is_target(self, target):

        return self.platform == target


compiler_platform = CompilerPlatform()
