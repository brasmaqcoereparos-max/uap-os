class ParallelExecutor:
    def __init__(self):
        self.tasks = []
        self.results = []
        self.errors = []

    def add(
        self,
        task,
        name=None,
        enabled=True,
    ):
        item = {
            "name": (
                str(name)
                if name is not None
                else f"task_{len(self.tasks) + 1}"
            ),
            "task": task,
            "enabled": bool(enabled),
        }

        self.tasks.append(item)

        return item

    def remove(self, index):
        index = int(index)

        if not 0 <= index < len(
            self.tasks
        ):
            return False

        self.tasks.pop(index)

        return True

    def clear(self):
        self.tasks.clear()
        self.results.clear()
        self.errors.clear()

    def list_tasks(self):
        return list(self.tasks)

    @staticmethod
    def _execute_task(
        task,
        context=None,
    ):
        if callable(task):
            try:
                return task(
                    context or {}
                )
            except TypeError:
                return task()

        execute = getattr(
            task,
            "execute",
            None,
        )

        if callable(execute):
            try:
                return execute(
                    context or {}
                )
            except TypeError:
                return execute()

        run = getattr(
            task,
            "run",
            None,
        )

        if callable(run):
            try:
                return run(
                    context or {}
                )
            except TypeError:
                return run()

        return task

    def execute(
        self,
        context=None,
        stop_on_error=False,
    ):
        self.results = []
        self.errors = []

        for item in self.tasks:
            if not item["enabled"]:
                continue

            try:
                result = (
                    self._execute_task(
                        item["task"],
                        context=context,
                    )
                )

                self.results.append({
                    "name": item["name"],
                    "success": True,
                    "result": result,
                })

            except Exception as exc:
                error = {
                    "name": item["name"],
                    "success": False,
                    "error": str(exc),
                }

                self.errors.append(error)
                self.results.append(error)

                if stop_on_error:
                    break

        return {
            "success": (
                len(self.errors) == 0
            ),
            "results": list(
                self.results
            ),
            "errors": list(
                self.errors
            ),
        }


parallel_executor = ParallelExecutor()
