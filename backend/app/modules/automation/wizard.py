class AutomationWizard:

    def __init__(self):

        self.steps = []
        self.current_step = 0

    def add_step(
        self,
        title,
        description,
    ):

        self.steps.append(
            {
                "title": title,
                "description": description,
            }
        )

    def next(self):

        if self.current_step < len(self.steps) - 1:
            self.current_step += 1

        return self.current()

    def previous(self):

        if self.current_step > 0:
            self.current_step -= 1

        return self.current()

    def current(self):

        if not self.steps:
            return None

        return self.steps[self.current_step]

    def reset(self):

        self.current_step = 0
