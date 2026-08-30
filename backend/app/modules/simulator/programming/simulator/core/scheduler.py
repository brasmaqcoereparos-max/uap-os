"""
Scheduler leve do núcleo do simulador UAP.

Contrato original preservado:

    scheduler.tasks
    scheduler.add(task)
    scheduler.execute()
    scheduler.clear()

O scheduler continua aceitando tarefas simples chamáveis,
mas agora suporta identificação, habilitação, remoção,
execução segura e estatísticas.
"""


class Scheduler:

    def __init__(self):
        self.tasks = []

        self.enabled = True
        self.running = False

        self.execute_count = 0
        self.task_execution_count = 0
        self.error_count = 0

        self.last_error = None

    def add(
        self,
        task,
    ):
        if task is None:
            return None

        if not callable(task):
            raise TypeError(
                "A tarefa precisa ser executável."
            )

        self.tasks.append(
            task
        )

        return task

    def remove(
        self,
        task,
    ):
        if task not in self.tasks:
            return False

        self.tasks.remove(
            task
        )

        return True

    def contains(
        self,
        task,
    ):
        return (
            task in self.tasks
        )

    def execute(self):
        if not self.enabled:
            return []

        self.running = True

        results = []

        try:
            for task in list(
                self.tasks
            ):
                try:
                    result = task()

                    results.append(
                        result
                    )

                    self.task_execution_count += 1

                except Exception as exc:
                    self.error_count += 1
                    self.last_error = str(exc)

                    raise

            self.execute_count += 1
            self.last_error = None

            return results

        finally:
            self.running = False

    def execute_one(
        self,
        task,
    ):
        if not callable(task):
            raise TypeError(
                "A tarefa precisa ser executável."
            )

        try:
            result = task()

            self.task_execution_count += 1
            self.last_error = None

            return result

        except Exception as exc:
            self.error_count += 1
            self.last_error = str(exc)

            raise

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False
        self.running = False

        return True

    def count(self):
        return len(
            self.tasks
        )

    def empty(self):
        return (
            len(self.tasks)
            == 0
        )

    def all(self):
        return list(
            self.tasks
        )

    def clear(self):
        count = len(
            self.tasks
        )

        self.tasks.clear()

        return count

    def reset(self):
        self.clear()

        self.running = False

        self.execute_count = 0
        self.task_execution_count = 0
        self.error_count = 0

        self.last_error = None

        return True

    def status(self):
        return {
            "enabled": self.enabled,
            "running": self.running,
            "task_count": (
                self.count()
            ),
            "execute_count": (
                self.execute_count
            ),
            "task_execution_count": (
                self.task_execution_count
            ),
            "error_count": (
                self.error_count
            ),
            "last_error": (
                self.last_error
            ),
        }

    def to_dict(self):
        return self.status()


scheduler = Scheduler()
