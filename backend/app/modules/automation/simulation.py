import time


class AutomationSimulation:
    def __init__(self):
        self.running = False
        self.paused = False

        self.results = []
        self.context = {}

        self.started_at = None
        self.finished_at = None

    def start(self, context=None):
        self.running = True
        self.paused = False

        self.results.clear()

        self.context = dict(
            context or {}
        )

        self.started_at = time.time()
        self.finished_at = None

        return True

    def stop(self):
        self.running = False
        self.paused = False
        self.finished_at = time.time()

        return True

    def pause(self):
        if not self.running:
            return False

        self.paused = True
        return True

    def resume(self):
        if not self.running:
            return False

        self.paused = False
        return True

    def add_result(
        self,
        step,
        result,
        success=True,
        metadata=None,
    ):
        entry = {
            "index": len(
                self.results
            ),
            "step": step,
            "result": result,
            "success": bool(success),
            "metadata": dict(
                metadata or {}
            ),
            "timestamp": time.time(),
        }

        self.results.append(entry)

        return entry

    def execute_step(
        self,
        step,
        action,
    ):
        if (
            not self.running
            or self.paused
        ):
            return None

        try:
            if callable(action):
                try:
                    result = action(
                        self.context
                    )
                except TypeError:
                    result = action()

            else:
                execute = getattr(
                    action,
                    "execute",
                    None,
                )

                if callable(execute):
                    try:
                        result = execute(
                            self.context
                        )
                    except TypeError:
                        result = execute()
                else:
                    result = action

            return self.add_result(
                step,
                result,
                success=True,
            )

        except Exception as exc:
            return self.add_result(
                step,
                None,
                success=False,
                metadata={
                    "error": str(exc)
                },
            )

    def get_results(self):
        return list(self.results)

    def clear(self):
        self.results.clear()

    def status(self):
        return {
            "running": self.running,
            "paused": self.paused,
            "results": len(
                self.results
            ),
            "started_at": (
                self.started_at
            ),
            "finished_at": (
                self.finished_at
            ),
        }


automation_simulation = (
    AutomationSimulation()
        )
