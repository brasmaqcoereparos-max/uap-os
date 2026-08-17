class NavigationQueue:

    def __init__(self):

        self.commands = []

    def add(self, command):

        self.commands.append(command)

    def next(self):

        if not self.commands:

            return None

        return self.commands.pop(0)

    def clear(self):

        self.commands.clear()

    def is_empty(self):

        return not self.commands

    def get_all(self):

        return list(self.commands)
