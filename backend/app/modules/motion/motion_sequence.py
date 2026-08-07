class MotionSequence:

    def __init__(

        self,

        name,

    ):

        self.name = name

        self.steps = []

    def add_step(

        self,

        step,

    ):

        self.steps.append(step)

    def remove_step(

        self,

        index,

    ):

        if 0 <= index < len(self.steps):

            self.steps.pop(index)

    def clear(self):

        self.steps.clear()

    def count(self):

        return len(self.steps)
