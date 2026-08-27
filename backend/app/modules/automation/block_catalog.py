from app.modules.automation.block_description import (
    BlockDescription,
)

from app.modules.automation.block_library import (
    block_library,
)


class BlockCatalog:
    def __init__(self):
        self.items = {}
        self.metadata = {}

    def register(
        self,
        block_type,
        name,
        simple_description,
        technical_description="",
        category="basic",
        icon="",
        tags=None,
        user_levels=None,
    ):
        key = str(block_type)

        self.items[key] = (
            BlockDescription(
                name,
                simple_description,
                technical_description,
            )
        )

        self.metadata[key] = {
            "category": str(category),
            "icon": str(icon),
            "tags": list(
                tags or []
            ),
            "user_levels": list(
                user_levels
                or [
                    "beginner",
                    "intermediate",
                    "professional",
                ]
            ),
        }

        return self.items[key]

    def unregister(
        self,
        block_type,
    ):
        key = str(block_type)

        self.metadata.pop(
            key,
            None,
        )

        return self.items.pop(
            key,
            None,
        )

    def get(
        self,
        block_type,
    ):
        return self.items.get(
            str(block_type)
        )

    def get_entry(
        self,
        block_type,
    ):
        key = str(block_type)

        description = (
            self.items.get(key)
        )

        if description is None:
            return None

        result = {
            "type": key,
            "name": getattr(
                description,
                "name",
                key,
            ),
            "simple_description": getattr(
                description,
                "simple_description",
                "",
            ),
            "technical_description": (
                getattr(
                    description,
                    "technical_description",
                    "",
                )
            ),
        }

        result.update(
            self.metadata.get(
                key,
                {},
            )
        )

        template = block_library.get(
            key
        )

        if template is not None:
            result["template"] = (
                template.to_dict()
            )

        return result

    def list(
        self,
        category=None,
        user_level=None,
    ):
        result = []

        for key in self.items:
            entry = self.get_entry(
                key
            )

            meta = self.metadata.get(
                key,
                {},
            )

            if (
                category is not None
                and meta.get(
                    "category"
                )
                != str(category)
            ):
                continue

            if (
                user_level is not None
                and str(user_level)
                not in meta.get(
                    "user_levels",
                    [],
                )
            ):
                continue

            result.append(
                entry
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

        if not query:
            return self.list(
                user_level=user_level
            )

        return [
            entry
            for entry
            in self.list(
                user_level=user_level
            )
            if query
            in str(entry).lower()
        ]

    def count(self):
        return len(
            self.items
        )


block_catalog = BlockCatalog()
