class AutomationSimulation:

    def __init__(self):

        self.running = False
        self.results = []

    def start(self):

        self.running = True
        self.results.clear()

    def stop(self):

        self.running = False

    def add_result(
        self,
        step,
        result,
    ):

        self.results.append(
            {
                "step": step,
                "result": result,
            }
        )

    def get_results(self):

        return list(self.results)
