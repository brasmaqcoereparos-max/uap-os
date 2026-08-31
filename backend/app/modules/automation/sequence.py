"""
Sequência ordenada de ações da automação UAP.
"""


class AutomationSequence:

    def __init__(
        self,
        name,
        description="",
        metadata=None,
    ):
        self.name = str(
            name
        )

        self.description = str(
            description
        )

        self.steps = []

        self.enabled = True

        self.metadata = dict(
            metadata or {}
        )

        self.execution_count = 0
        self.last_result = None

    def add_step(
        self,
        step,
        name=None,
        enabled=True,
        metadata=None,
    ):
        item = {
            "name": (
                str(name)
                if name is not None
                else (
                    f"step_"
                    f"{len(self.steps) + 1}"
                )
            ),
            "action": step,
            "enabled": bool(
                enabled
            ),
            "metadata": dict(
                metadata or {}
            ),
        }

        self.steps.append(
            item
        )

        return item

    def insert_step(
        self,
        index,
        step,
        name=None,
        enabled=True,
    ):
        index = max(
            0,
            min(
                int(index),
                len(self.steps),
            ),
        )

        item = {
            "name": (
                str(name)
                if name is not None
                else f"step_{index + 1}"
            ),
            "action": step,
            "enabled": bool(
                enabled
            ),
            "metadata": {},
        }

        self.steps.insert(
            index,
            item,
        )

        return item

    def remove_step(
        self,
        index,
    ):
        index = int(
            index
        )

        if not (
            0
            <= index
            < len(self.steps)
        ):
            return False

        self.steps.pop(
            index
        )

        return True

    def move_step(
        self,
        source,
        target,
    ):
        source = int(
            source
        )

        target = int(
            target
        )

        if not (
            0
            <= source
            < len(self.steps)
        ):
            return False

        step = self.steps.pop(
            source
        )

        target = max(
            0,
            min(
                target,
                len(self.steps),
            ),
        )

        self.steps.insert(
            target,
            step,
        )

        return True

    def enable_step(
        self,
        index,
    ):
        self.steps[
            int(index)
        ]["enabled"] = True

        return True

    def disable_step(
        self,
        index,
    ):
        self.steps[
            int(index)
        ]["enabled"] = False

        return True

    def get_step(
        self,
        index,
    ):
        index = int(
            index
        )

        if not (
            0
            <= index
            < len(self.steps)
        ):
            return None

        return self.steps[
            index
        ]

    def clear(self):
        count = len(
            self.steps
        )

        self.steps.clear()

        return count

    def list_steps(self):
        return list(
            self.steps
        )

    def count(self):
        return len(
            self.steps
        )

    def enable(self):
        self.enabled = True

        return self

    def disable(self):
        self.enabled = False

        return self

    def reset_statistics(self):
        self.execution_count = 0
        self.last_result = None

        return True

    def to_dict(self):
        result = []

        for index, step in enumerate(
            self.steps
        ):
            action = step[
                "action"
            ]

            serializer = getattr(
                action,
                "to_dict",
                None,
            )

            result.append({
                "index": index,
                "name": step["name"],
                "enabled": (
                    step["enabled"]
                ),
                "action": (
                    serializer()
                    if callable(serializer)
                    else str(action)
                ),
                "metadata": dict(
                    step["metadata"]
                ),
            })

        return {
            "name": self.name,
            "description": (
                self.description
            ),
            "enabled": (
                self.enabled
            ),
            "steps": result,
            "metadata": dict(
                self.metadata
            ),
            "execution_count": (
                self.execution_count
            ),
            "last_result": (
                self.last_result
            ),
                    }
