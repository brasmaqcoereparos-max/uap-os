import time
import uuid


class AutomationHistory:
    def __init__(
        self,
        max_entries=1000,
    ):
        self.entries = []

        self.max_entries = int(
            max_entries
        )

    def add(
        self,
        action,
        data=None,
        source=None,
        level="info",
    ):
        entry = {
            "id": str(
                uuid.uuid4()
            ),
            "action": str(action),
            "data": dict(
                data or {}
            ),
            "source": source,
            "level": str(level),
            "timestamp": (
                time.time()
            ),
        }

        self.entries.append(
            entry
        )

        if (
            self.max_entries > 0
            and len(self.entries)
            > self.max_entries
        ):
            excess = (
                len(self.entries)
                - self.max_entries
            )

            del self.entries[
                :excess
            ]

        return entry

    def list(
        self,
        limit=None,
        action=None,
        level=None,
    ):
        result = list(
            self.entries
        )

        if action is not None:
            result = [
                item
                for item in result
                if item["action"]
                == str(action)
            ]

        if level is not None:
            result = [
                item
                for item in result
                if item["level"]
                == str(level)
            ]

        if limit is not None:
            limit = max(
                0,
                int(limit),
            )

            result = result[
                -limit:
            ]

        return result

    def latest(self):
        if not self.entries:
            return None

        return self.entries[-1]

    def clear(self):
        count = len(
            self.entries
        )

        self.entries.clear()

        return count

    def count(self):
        return len(
            self.entries
        )

    def to_dict(self):
        return {
            "count": self.count(),
            "max_entries": (
                self.max_entries
            ),
            "entries": self.list(),
        }


automation_history = (
    AutomationHistory()
        )
