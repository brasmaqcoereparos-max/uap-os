class ContextHelp:
    def __init__(self):
        self.help_items = {}

    def register(
        self,
        key,
        title,
        description,
        example="",
        technical_description="",
        tips=None,
        warnings=None,
        user_levels=None,
        metadata=None,
    ):
        key = str(key)

        self.help_items[key] = {
            "key": key,
            "title": str(title),
            "description": str(description),
            "technical_description": str(
                technical_description
            ),
            "example": str(example),
            "tips": list(tips or []),
            "warnings": list(warnings or []),
            "user_levels": list(
                user_levels
                or [
                    "beginner",
                    "intermediate",
                    "professional",
                ]
            ),
            "metadata": dict(metadata or {}),
        }

        return self.help_items[key]

    def unregister(self, key):
        return self.help_items.pop(
            str(key),
            None,
        )

    def get(
        self,
        key,
        user_level=None,
    ):
        item = self.help_items.get(
            str(key)
        )

        if item is None:
            return None

        result = dict(item)

        if user_level is not None:
            level = str(
                getattr(
                    user_level,
                    "value",
                    user_level,
                )
            ).strip().lower()

            if (
                level
                not in result["user_levels"]
            ):
                return None

            if level in {
                "professional",
                "profissional",
            }:
                result["description"] = (
                    result[
                        "technical_description"
                    ]
                    or result["description"]
                )

        return result

    def search(
        self,
        text,
        user_level=None,
    ):
        query = str(
            text
        ).strip().lower()

        result = []

        for key in self.help_items:
            item = self.get(
                key,
                user_level=user_level,
            )

            if item is None:
                continue

            if (
                not query
                or query
                in str(item).lower()
            ):
                result.append(item)

        return result

    def list(
        self,
        user_level=None,
    ):
        if user_level is None:
            return {
                key: dict(value)
                for key, value
                in self.help_items.items()
            }

        return {
            key: item
            for key in self.help_items
            if (
                item := self.get(
                    key,
                    user_level=user_level,
                )
            )
            is not None
        }

    def clear(self):
        self.help_items.clear()

    def count(self):
        return len(self.help_items)


context_help = ContextHelp()
