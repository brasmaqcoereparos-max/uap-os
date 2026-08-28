class AutomationLoop:
    def __init__(
        self,
        max_iterations=None,
    ):
        self.enabled = False

        self.max_iterations = (
            int(max_iterations)
            if max_iterations
            is not None
            else None
        )

        if (
            self.max_iterations
            is not None
            and self.max_iterations < 0
        ):
            raise ValueError(
                "max_iterations não "
                "pode ser negativo."
            )

        self.iteration = 0

    def start(self):
        self.enabled = True
        self.iteration = 0

        return True

    def stop(self):
        self.enabled = False
        return True

    def reset(self):
        self.enabled = False
        self.iteration = 0

    def can_continue(self):
        if not self.enabled:
            return False

        if self.max_iterations is None:
            return True

        return (
            self.iteration
            < self.max_iterations
        )

    def next(self):
        if not self.can_continue():
            self.stop()
            return False

        self.iteration += 1

        if (
            self.max_iterations
            is not None
            and self.iteration
            >= self.max_iterations
        ):
            self.enabled = False

        return True

    def run(
        self,
        callback,
        context=None,
    ):
        if not callable(callback):
            raise TypeError(
                "callback precisa "
                "ser executável."
            )

        self.start()

        results = []

        while self.can_continue():
            try:
                result = callback(
                    self.iteration,
                    context or {},
                )
            except TypeError:
                result = callback()

            results.append(
                result
            )

            self.next()

        return results

    def is_running(self):
        return self.enabled

    def to_dict(self):
        return {
            "enabled": self.enabled,
            "iteration": (
                self.iteration
            ),
            "max_iterations": (
                self.max_iterations
            ),
    }
